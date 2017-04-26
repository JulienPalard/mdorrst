# Tstat (TCP STatistic and Analysis Tool) Transport Tools

Client programs to read a tstat file hierarchy, parse the logs, convert them to JSON objects, and send them to a remote archive (like a RabbitMQ server). This tool was originally developed to support the [National Science Foundation NetSage Project](http://www.netsage.global/home).

## Overview

### tstat_send

When invoked, it crawls a tstat file hierarchy laid out like this:

    tstat/2016_02_17_12_53.out:
    total 808
    -rw-r--r--@ root users  135103 Feb 17 13:54 log_tcp_complete
    -rw-r--r--@ root users  277154 Feb 17 13:54 log_udp_complete

    tstat/2016_02_17_13_54.out:
    total 792
    -rw-r--r--@ root users  123801 Feb 17 14:54 log_tcp_complete
    -rw-r--r--@ root users  278301 Feb 17 14:54 log_udp_complete

Selected data are extracted from the logs, formatted into JSON objects, and lists of the objects are sent to a remote server for archiving. The objects from a single set of logs log are broken into a series of smaller lists (up to 100 objects per list). Each "sub-list" gets sent to the remote server so no one single send operation swamps the remote server.

When the logs in each directory have been successfully processed (the data have been sent, delivery confirmations received, etc), a dotfile named `.processed` will be dropped in that directory. That marks that directory as processed, and those logs will be ignored on subsequent runs. The `tstat_cull` utility similarly uses the .processed dotfiles to prune old logs.

It is not a persistent process and would be run periodically from cron (for example) to periodically process logs on a "live" machine.

Currently, the only "transport" that is supported is sending the JSON to a RabbitMQ server, but it would be relatively straightforward to implement other transports like using HTTP to send to a REST API.

## Usage

### tstat_send arguments

#### Required

##### --directory

Path to the "root" of the directory structure where tstat writes the timestamped directories and logfiles. No default.

##### --config

Path to the .ini style config file used to pass configuration directives to the underlying transport code.

Default: `./config.ini`

#### Optional

##### --threshold

The transfer threshold in megabytes. Any transfer below this threshold below will be ignored.

Default: `1000`

##### --transport

Specify the underlying transport to send the JSON over. Currently, only RabbitMQ is supported.

Default: `rabbit`

##### --sensor

The sensor_id element of the message metadata defaults to `socket.gethostname()` - using this flag will set that value manually.

##### --single

Process a single "timestamped directory" of files, send JSON and exit. This is primarily for development or debugging.

##### --no-transport

Skips sending the messages to the selected transport and dumps them to standard out instead. Use standard shell redirection `... --no-transport > file.json` to save output to a file.

##### --verbose and --debug

`--verbose` triggers additional log output. `--debug` changes the log level to `logging.DEBUG` in the transport module. This is primarily for debugging connection problems with RabbitMQ, or to get detailed output on the transactions with the remote server.

## Config file

`tstat_send` uses an .ini style configuration file to pass options to the underlying transport code. Doing this with command-line args would be too ponderous. Example config file:

    [rabbit]
    # host/port are required for all transport variants
    host = localhost
    # this is the rabbit ssl port, if not, use default 5672 or custom port
    port = 5671
    # these are required for some transports
    username = esnet
    password = some_mysterious_password
    use_ssl = True
    # these are rabbit specific - the exchange key is required
    # even if you don't set the value to anything/use the default "".
    vhost = netsage
    queue = netsage_tstat
    routing_key = netsage_tstat
    exchange =

    # This is an optional stanza. The key/value pairs
    # will be passed to channel.queue_declare() as kwargs
    # (ie: durable, exclusive, auto_delete, etc).
    [rabbit_queue_options]

    # This is an optional stanza. The key/value pairs
    # will generate a dict to be passed as kwargs to ssl.wrap_socket()
    # https://docs.python.org/2/library/ssl.html#ssl.wrap_socket
    [ssl_options]

* The values `host` and `port` will be required for all transport variants. If they are not supplied, a configuration error occur.
* The rabbit transport requires the `username` and `password` config values. They may also be enabled in other transport variants.
* `vhost, queue, routing_key and exchange` should be self-explanatory RabbitMQ directives.
* The `rabbit_queue_options` stanza is optional and can be used to pass additional kwargs to `queue_declare()` if need be. By default the code only passes the `queue` argument with the name of the queue.
* The `ssl_options` stanza is optional too. Only necessary if additional args (paths to keyfiles, etc) need to be passed to the underlying `ssl` library.

## Message format

Every log line may generate zero, one or two JSON objects. This depends on the threshold set with the `--bits` flag and what kind of transfer it is. The generated objects will be sub-divided into a series of lists of up to 100 objects each. That way, each send operation is of a manageable size rather than sending one huge list.

All numeric values are being converted to "actual" numeric types. All floating point values are being rounded to three decimal places to avoid small values being rendered in scientific notation. Timestamps logged in floating point ms are being converted to integer epoch seconds.

### UDP logs

This is the most basic/common format.

    {
        "interval": 600,
        "values": {
            "duration": 0.0,
            "num_bits": 544,
            "num_packets": 1
        },
        "meta": {
            "src_ip": "198.129.77.102",
            "src_port": 123,
            "dst_ip": "198.124.252.130",
            "dst_port": 123,
            "protocol": "udp"
        },
        "start": 1455745857,
        "end": 1455745857
    },

### TCP logs

The TCP logs are identical, but have additional values in the `values` stanza:

    {
        "interval": 600,
        "values": {
            "duration": 191.796,
            "num_bits": 22120,
            "num_packets": 14,
            "tcp_rexmit_bytes": 0,
            "tcp_rexmit_pkts": 0,
            "tcp_rtt_avg": 4.442,
            "tcp_rtt_min": 0.007,
            "tcp_rtt_max": 39.094,
            "tcp_rtt_std": 10.648,
            "tcp_pkts_rto": 0,
            "tcp_pkts_fs": 0,
            "tcp_pkts_reor": 0,
            "tcp_pkts_dup": 0,
            "tcp_pkts_unk": 0,
            "tcp_pkts_fc": 0,
            "tcp_pkts_unrto": 0,
            "tcp_pkts_unfs": 0,
            "tcp_cwin_min": 16,
            "tcp_cwin_max": 960,
            "tcp_out_seq_pkts": 0,
            "tcp_window_scale": 7,
            "tcp_mss": 1460,
            "tcp_max_seg_size": 960,
            "tcp_min_seg_size": 16,
            "tcp_win_max": 960,
            "tcp_win_min": 16,
            "tcp_initial_cwin": 21
        },
        "meta": {
            "src_ip": "198.128.14.246",
            "src_port": 58635,
            "dst_ip": "198.129.77.102",
            "dst_port": 22,
            "protocol": "tcp"
        },
        "start": 1455698490,
        "end": 1455698490
    },

## Utility programs

### tstat_cull

Crawls a tstat directory to cull processed logs from disk.  Tstat can generate a lot of output, this cleans up processed files, while leaving a configurable "buffer" of time to keep processed logs. The default is too keep 2 days worth of processed logs on disk, rather than deleting them right after they have been processed.

This script checks the `mtime` of the `.processed` state file in a directory of processed logs. If it is older than the `--ttl` time to live in hours (default: 48), the directory and logs are removed.

#### Required args

##### --directory

This is the path to the "root" of the directory structure where tstat writes the timestamped directories and logfiles. No default.

#### Optional args

##### --ttl

The time to live in hours.  Set this if you don't want to use the default of 48 hours.

##### --dry-run

Do a dry run. Just log the directories that will be deleted but don't delete them.

## Extending tstat_send with additional transports

Adding additional transports is fairly straightforward.

See doc/extending.md in the source distribution.