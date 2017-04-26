Password Stretcher
==================

Derive high-entropy passwords from passphrases using a slow key derivation function (sometimes referred to as [key stretching](https://en.wikipedia.org/wiki/Key_stretching)).

Why?
----

Password stretching makes it significantly harder to guess the password for a hash/file encryption key/etc. since an attacker has to use more resources or wait longer for each password they try.

Many programs that use passwords for securing sensitive information do not have particularly complex password stretching/key derivation algorithms (e.g. GPG), which make them vulnerable to password cracking, unless a particularly long and complex passphrase is used.

`stretch-pass` allows you to generate long, high-entropy passwords from a passphrase using a slow key derivation function, which can then be used in these programs.

Setup
=====

`$ pip3 install -r requirements.txt`

Usage
=====

To use stretch-pass with all the defaults:

`$ stretch-pass`

When you run this for the first time, the program will generate a random [salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) and store it in a config file (which defaults to `~/.stretchpassrc`).

You'll be prompted for a passphrase; this will be used to deterministically generate a long, random password to be used in another application. The passphrase you enter is not stored anywhere. You can use different passphrases for different applications.

If you want the generated password to be put into the clipboard instead of printed to the terminal, add `-c` or `--clip`.

Adding `-C` or `--confirm` will prompt for the passphrase twice to verify that it was entered correctly.

Key Derivation Function Parameters
----------------------------------

You can change the KDF parameters in order to increase the computational resources required to guess a passphrase. You can change the time cost (CPU load), memory cost (RAM consumption), and parallelism (usage across multiple cores). Use `stretch-pass --kdf-params` to print the parameters it is currently using, then use the `-t`, `-m`, and `-p` options to tweak them to meet your requirements. Note that the default parameters are deliberately very high, so you may wish to try lowering them if it takes too long to generate the password. You can also change the output password length using `-l`.

Once you've found some suitable parameters, you can put them in the config file. To easily edit the config file, make sure your `EDITOR` environment variable is set and run `stretch-pass -e`, which will open the config file in the editor of your choice.

The config file is a simple list of key/value pairs, in any order. All entries except `SALT` are optional. For example:

```
# This is a comment

# Spacing around '=' is optional
TIME_COST = 32
MEMORY_COST = 131072
PARALLELISM = 2
PASSWORD_LENGTH = 64
SALT = 00112233445566778899aabbccddeeff
```

**N.B: Changing any of these parameters will result in a different password to be generated from the same passphrase! Configure these parameters *before* using the generated passwords, and backup the configuration file somewhere safe.**

Autocomplete
------------

stretch-pass can use [argcomplete](https://github.com/kislyuk/argcomplete) for tab completion, but this is optional.

Full Help
---------

```
$ stretch-pass -h
usage: stretch-pass [-h] [-v] [-V] [--log-file LOG_FILE]
                    [--config CONFIG_PATH] [-e] [--kdf-params] [-t TIME_COST]
                    [-m MEMORY_COST] [-p PARALLELISM] [-l PASSWORD_LENGTH]
                    [-s SALT] [-u USERNAME] [-c]
                    [--passphrase PASSPHRASE | --stdin-passphrase | -C]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose
  -V, --version         Show version and exit
  --log-file LOG_FILE   Path to log file (use with --verbose)
  --config CONFIG_PATH  Path to config file (defaults to ~/.stretchpassrc)
  -e, --edit-config     Opens the stretch-pass config using EDITOR
  --kdf-params          Print KDF parameters and exit
  -t TIME_COST, --time-cost TIME_COST
  -m MEMORY_COST, --memory-cost MEMORY_COST
  -p PARALLELISM, --parallelism PARALLELISM
  -l PASSWORD_LENGTH, --password-length PASSWORD_LENGTH
  -s SALT, --salt SALT  The hex string to use as a salt (at least 8 bytes)
  -u USERNAME, --username USERNAME
                        Username/program name (case sensitive - used to
                        generate the password)
  -c, --clip            Copy the password to clipboard instead of STDOUT
  --passphrase PASSPHRASE
                        Pass passphrase directly instead of via prompt
  --stdin-passphrase    Read passphrase from STDIN (be aware of newline
                        characters and environment encodings)
  -C, --confirm         Prompt for the passphrase twice and verify they are
                        the same
```
