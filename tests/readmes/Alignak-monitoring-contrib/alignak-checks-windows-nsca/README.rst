Alignak checks package for Windows passively checked hosts/services
===================================================================

*Checks pack for monitoring Windows hosts with NSCA passive checks*


.. image:: https://badge.fury.io/py/alignak_checks_windows_nsca.svg
    :target: https://badge.fury.io/py/alignak-checks-windows-nsca
    :alt: Most recent PyPi version

.. image:: https://img.shields.io/badge/IRC-%23alignak-1e72ff.svg?style=flat
    :target: http://webchat.freenode.net/?channels=%23alignak
    :alt: Join the chat #alignak on freenode.net

.. image:: https://img.shields.io/badge/License-AGPL%20v3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0
    :alt: License AGPL v3

Installation
------------

The installation of this checks pack will copy some configuration files in the Alignak default configuration directory (eg. */usr/local/etc/alignak*). The copied files are located in the default sub-directory used for the packs (eg. *arbiter/packs*).

From PyPI
~~~~~~~~~
To install the package from PyPI:
::

   sudo pip install alignak-checks-windows-nsca


From source files
~~~~~~~~~~~~~~~~~
To install the package from the source files:
::

   git clone https://github.com/Alignak-monitoring-contrib/alignak-checks-windows-nsca
   cd alignak-checks-windows-nsca
   sudo pip install .

**Note:** *using `sudo python setup.py install` will not correctly manage the package configuration files! The recommended way is really to use `pip`;)*

Documentation
-------------

Configuration
~~~~~~~~~~~~~
This checks pack do not need any specific configuration.


Prepare Windows host
~~~~~~~~~~~~~~~~~~~~
Some operations are necessary on the Windows monitored hosts if NSClient++ is not yet installed and running.

Install and configure NSClient++ for scheduled NSCA checks.

The first example below is an NSClient configuration file and it schedules the NSCa checks with the default NSClient pre-installed commands (see alias). The second example is an NSClient registry configuration that defines its own commands in the NSCA scheduled checks. Anyway, for more information, we invite you to consult the `NSClient ++ Web site <https://www.nsclient.org/>`_.

NSClient++ Ini file configuration example:

::

    [/modules]
    CheckDisk = 1
    CheckEventLog = 1
    CheckExternalScripts = 1
    CheckHelpers = 1
    CheckNSCP = 1
    CheckSystem = 1
    CheckWMI = 1
    NSCAClient = 1
    Scheduler = 1

    [/settings/default]
    ; Alignak server Ip address
    allowed hosts = address = 192.168.15.1

    [/settings/external scripts/alias]
    alias_cpu = checkCPU warn=80 crit=90 time=5m time=1m time=30s
    alias_cpu_ex = checkCPU warn=$ARG1$ crit=$ARG2$ time=5m time=1m time=30s
    alias_disk = CheckDriveSize MinWarn=10% MinCrit=5% CheckAll FilterType=FIXED
    alias_disk_loose = CheckDriveSize MinWarn=10% MinCrit=5% CheckAll FilterType=FIXED ignore-unreadable
    alias_event_log = CheckEventLog file=application file=system MaxWarn=1 MaxCrit=1 "filter=generated gt -2d AND severity NOT IN ('success', 'informational') AND source != 'SideBySide'" truncate=800 unique descriptions "syntax=%severity%: %source%: %message% (%count%)"
    alias_file_age = checkFile2 filter=out "file=$ARG1$" filter-written=>1d MaxWarn=1 MaxCrit=1 "syntax=%filename% %write%"
    alias_file_size = CheckFiles "filter=size > $ARG2$" "path=$ARG1$" MaxWarn=1 MaxCrit=1 "syntax=%filename% %size%" max-dir-depth=10
    alias_mem = checkMem MaxWarn=80% MaxCrit=90% ShowAll=long type=physical type=virtual type=paged type=page
    alias_process = checkProcState "$ARG1$=started"
    alias_process_count = checkProcState MaxWarnCount=$ARG2$ MaxCritCount=$ARG3$ "$ARG1$=started"
    alias_process_hung = checkProcState MaxWarnCount=1 MaxCritCount=1 "$ARG1$=hung"
    alias_process_stopped = checkProcState "$ARG1$=stopped"
    alias_sched_all = CheckTaskSched "filter=exit_code ne 0" "syntax=%title%: %exit_code%" warn=>0
    alias_sched_long = CheckTaskSched "filter=status = 'running' AND most_recent_run_time < -$ARG1$" "syntax=%title% (%most_recent_run_time%)" warn=>0
    alias_sched_task = CheckTaskSched "filter=title eq '$ARG1$' AND exit_code ne 0" "syntax=%title% (%most_recent_run_time%)" warn=>0
    alias_service = checkServiceState CheckAll
    alias_service_ex = checkServiceState CheckAll "exclude=Net Driver HPZ12" "exclude=Pml Driver HPZ12" exclude=stisvc
    alias_up = checkUpTime MinWarn=1d MinWarn=1h
    alias_updates = check_updates -warning 0 -critical 0
    alias_volumes = CheckDriveSize MinWarn=10% MinCrit=5% CheckAll=volumes FilterType=FIXED
    alias_volumes_loose = CheckDriveSize MinWarn=10% MinCrit=5% CheckAll=volumes FilterType=FIXED ignore-unreadable
    default =

    [/settings/scheduler]
    threads = 5

    [/settings/scheduler/schedules/default]
    channel = NSCA
    interval = 300s
    report = all

    [/settings/scheduler/schedules]

    ; Services to be checked
    nsca_cpu = alias_cpu
    nsca_memory = alias_mem
    nsca_disk = alias_disk
    nsca_uptime = alias_up
    nsca_services = alias_service_ex

    [/settings/NSCA/client]
    channel = NSCA

    ; The same host name configured in Alignak
    hostname = win2k8


    [/settings/NSCA/client/targets/default]

    ; Alignak server Ip address
    address = 192.168.15.1
    port = 5667
    allowed ciphers = ADH
    certificate =
    encryption =
    password = change-me
    timeout = 30
    use ssl = false
    verify mode = none


    [/settings/log]
    date format = %Y-%m-%d %H:%M:%S
    file name = ${exe-path}/nsclient.log
    level = info


    ; TODO
    [/settings/scheduler/schedules/check_alive]

    ; Undocumented key
    alias = host_check

    ; SCHEDULE COMMAND - Command to execute
    command = check_ok


    ; TODO
    [/settings/external scripts/wrappings]

    ; BATCH FILE WRAPPING -
    bat = scripts\\%SCRIPT% %ARGS%

    ; POWERSHELL WRAPPING -
    ps1 = cmd /c echo If (-Not (Test-Path "scripts\%SCRIPT%") ) { Write-Host "UNKNOWN: Script `"%SCRIPT%`" not found."; exit(3) }; scripts\%SCRIPT% $ARGS$; exit($lastexitcode) | powershell.exe /noprofile -command -

    ; VISUAL BASIC WRAPPING -
    vbs = cscript.exe //T:30 //NoLogo scripts\\lib\\wrapper.vbs %SCRIPT% %ARGS%


NSClient++ registry configuration example:

::

    Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++]

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\modules]
    "SyslogClient"="0"
    "Scheduler"="1"
    "NRPEServer"="1"
    "NRDPClient"="0"
    "SMTPClient"="0"
    "LUAScript"="0"
    "PythonScript"="0"
    "DotnetPlugins"="0"
    "CheckWMI"="1"
    "GraphiteClient"="0"
    "NRPEClient"="0"
    "SimpleFileWriter"="0"
    "CheckTaskSched"="1"
    "NSClientServer"="0"
    "CheckSystem"="1"
    "CheckExternalScripts"="1"
    "CheckHelpers"="1"
    "NSCAClient"="1"
    "CheckEventLog"="1"
    "SimpleCache"="0"
    "CheckLogFile"="0"
    "NSCAServer"="0"
    "CheckDisk"="1"
    "CheckNSCP"="1"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\NSCA]

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\NSCA\client]
    "hostname"="auto"
    "channel"="NSCA"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\NSCA\client\targets]

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\NSCA\client\targets\default]
    "use ssl"=dword:00000000
    "certificate"=""
    "allowed ciphers"=""
    "timeout"=dword:0000001e
    "verify mode"="none"
    "address"="alignak.net"
    "password"="alignak_nsca_receiver_password"
    "encryption"="xor"
    "payload length"="4096"
    "buffer length"="4096"
    "port"="5667"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler]
    "threads"=dword:00000005

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules]

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\check_alive]
    "alias"="host_check"
    "command"="check_ok"
    "interval"="300s"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\check_PC_cpu]
    "alias"="nsca_cpu"
    "command"="CheckCPU warn=75 crit=90 time=30m time=15m time=5m"
    "interval"="1800s"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\check_PC_disk]
    "alias"="nsca_disk"
    "command"="CheckDriveSize Drive=C: MaxWarn=75% MaxCrit=85%"
    "interval"="1800s"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\check_PC_memory]
    "alias"="nsca_memory"
    "command"="CheckMem MaxWarn=75% MaxCrit=90% ShowAll type=physical type=virtual type=paged type=page"
    "interval"="1800s"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\check_PC_uptime]
    "alias"="nsca_uptime"
    "command"="CheckUptime MaxCrit=25h MinWarn=35m"
    "interval"="1800s"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\check_swServices]
    "alias"="nsca_services"
    "command"="CheckServiceState CheckAll exclude=ShellHWDetection exclude=MMCSS exclude=clr_optimization_v4.0.30319_32 exclude=sppsvc exclude=StiSvc exclude=WMPNetworkSvc exclude=debugregsvc exclude=DoSvc exclude=MapsBroker exclude=CDPSvc exclude=WbioSrvc exclude=gpsvc exclude=tiledatamodelsvc exclude=wscsvc"
    "interval"="3600s"

    [HKEY_LOCAL_MACHINE\SOFTWARE\NSClient++\settings\scheduler\schedules\default]
    "target"="remote_host"
    "report"="all"
    "interval"="3600s"
    "channel"="NSCA"




Alignak configuration
~~~~~~~~~~~~~~~~~~~~~

You simply have to tag the concerned hosts with the template `windows-passive-host`.
::

    define host{
        use                     windows-passive-host
        host_name               my_windows_passive_host
        address                 0.0.0.0
    }

and this host will automatically inherit from the template parameters and services.


Bugs, issues and contributing
-----------------------------

Contributions to this project are welcome and encouraged ... `issues in the project repository <https://github.com/alignak-monitoring-contrib/alignak-checks-windows-nsca/issues>`_ are the common way to raise an information.
