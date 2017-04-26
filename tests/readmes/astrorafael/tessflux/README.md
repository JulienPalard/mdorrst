# TESSFLUX

MQTT to InfluxDB TESS data converter.

| Table of Contents                                                          |
|:---------------------------------------------------------------------------|
| [Description](README.md#Description)                                       |
| [Installation](README.md#Installation)                                     |
| [Configuration](README.md#Configuration)                                   |
| [Data Model](README.md#DataModel)                                          |
| [Logging]((README.md#Logging)                                              |

## <a name="Description"> Description

**tessflux** is a software package that listens to TESS data published to an MQTT broker and stores the readings in an [InfluxDB time series database](https://www.influxdata.com/open-source/#influxdb). Data written are suitable for real time monitoring through a [Grafana dashboard](http://grafana.org/). 

**tessflux** is being used as part of the [STARS4ALL Project](https://guaix.fis.ucm.es/splpr/TESS-V1).

TESS is an acronym for Telescope Encoder and Sky Sensor, a gadget designed by [Cristobal Garcia](http://www.observatorioremoto.com/TESS.pdf). The hardware version developed as part of the STARS4ALL Project is an inexpensive WiFi Sky Quality Meter using the same sensor as Unihedron Sky Quality Meter.

STARS4ALL is a European Awareness Platform for Sustainable and Social Innovation (CAPSSI) to protect the dark skies in Europe. Light pollution initiatives (LPIs) are developed to raising awareness about the consequences of artificial light at night on human well-being, biodiversity, visibility of stars, safety and energy waste.

## <a name="Instalation"> Instalation

Only for Linux.

  `sudo pip install tessflux`

  or from GitHub:

    git clone https://github.com/astrorafael/tessflux.git
    cd tessflux
    sudo python setup.py install


Type `tessflux -k` to start the service in foreground with console output

An available startup service script for debian-based systems is provided. 
Type `sudo service tessflux start` to start it.
Type `sudo update-rc.d tessflux defaults` to install it at boot time.

## <a name="Configuation"> TESSFLUX Configuation ###

The file `/etc/tessflux/config` provides the configuration options needed. This file is self explanatory. You **need to create** a new `config` file from the provided `/etc/tessflux/config.example`.

The Influx database and retention policies are defined in a `/etc/tessflux/influxdb.example`. You **need to create** a new `influxdb` Data Definition File with the database name and policies that suit your needs. See the [InfluxDB data retention documentation](https://docs.influxdata.com/influxdb/v1.2/guides/downsampling_and_retention/). Make sure that the database name specified here is the same as in the `/etc/tessflux/config` file

## <a name="DataModel"> Data Model ##

InfluxDB is a non-relational, schemaless, timeseries database. The *table* concept found in relational SQL maps into the *measurement* concept. The *column* concept found in traditional relational databases map either into *tags* or *fields* as appropiate.

    - A *tag* is the equivalent of column found in a *dimension table* in Dimensional modelling. 
    - A *field* is the equivalent of column found a *fact table* in Dimensional modelling. 

The data model created contains only **one measurement** whose name can be configured in `/etc/tessflux/config`) (i.e. `readings`) with the following tags:
- `name`,for the TESS name.

and the following fields:
- `mag`,  visual magnitude in magnitudeas/arcsec^2
- `freq`, the raw frequency measured by the light sensor.
- `tamb`, the ambient temperature at the TESS enclosure (ºC).
- `tsky`, the sky temperature sensed by a thermopile(ºC).

## <a name="Logging"> Logging ##

Log file is placed under `/var/log/tessflux.log`. 
Default log level is `info`. It generates very litte logging at this level.
The log is rotated through the /etc/logrotate.d/tessflux policy.

