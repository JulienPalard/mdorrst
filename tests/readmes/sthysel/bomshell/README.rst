========
Overview
========

.. image:: https://readthedocs.org/projects/bomshell/badge/?version=latest
   :target: http://bomshell.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


``bomshell`` is used to retrieve weather data from the `Australian Bureau of Meteorology's (BOM) <http://www.bom.gov.au/>`_
public ftpsite, and display the result in the shell, where it belongs, as God intended it.
Not this silly web clownsuit bullshit the kids are all agog about.

``bomshell`` retrieves the spatial data from the public ftp site and packs it into a local database. Tools are provided to
build and maintain the local database. Queries can be made of the database and the spatial database files. As the tool matures
the spatial database will be used to determine the product ID's of reports the user is interested in and those specific products
downloaded from the BOM's public ftp site.


Installation
============

.. code::

    $ pip install bomshell


Initial Setup
=============

Fetch the spatial data from BOM

.. code::

   $ bomshell spatial fetch


Build the local database. Table dumps are made from the original
data directly so its not needed for that.


.. code::
   
   $ bomshell spatial build

View some spatial data

.. code::
   
   $ bomshell spatial tabledump --spatial-type point_places | less -S
   


Sample Usage
============

All ``bomshell`` command line options are avilable from the ``--help`` option

.. code:: shell

    $ bomshell
    Usage: bomshell [OPTIONS] COMMAND [ARGS]...

      Retrieve weather data from the Australian Bureau of Meteorology

    Options:
      --version              Show the version and exit.
      -v, --verbose          Level of verbosity of logs
      -c, --cache-path PATH  BOM data cache path, Default:
                             /home/thys/.cache/bomshell
      --help                 Show this message and exit.

    Commands:
      spatial  Spatial database management


Sub-commands' options are also available using ``--help`` on the subcommand.

In order to know what the BOM calls a specific product you need to figure out
what the product ID is. This is available from the spatial databases. ``bomshell``
downloads the current spatial data and packs it into a convenient local database
that can be queried for, amongst other things, product ID's.

The local spatial database can be synced, or re-build as necessary.

.. code::

    $ bomshell spatial
    Usage: bomshell spatial [OPTIONS] COMMAND [ARGS]...

      Spatial database management

    Options:
      -o, --overwrite / --no-overwrite
                                      Overwrite existing spatial data, default is:
                                      False
      --help                          Show this message and exit.

    Commands:
      build      Build the local spatial database
      csvdump    Dump spatial data to csv
      fetch      Fetch spatial data
      sync       Sync the local spatial data, overwriting...
      tabledump  Dump spatial data to table

All spatial data can be printed to nicely formatted tables. Many output formats are available.

.. code::

    $ bomshell spatial tabledump --help
    Usage: bomshell spatial tabledump [OPTIONS]

      Dump spatial data to table

    Options:
      -s, --spatial-type [cyclone_areas|fire_districts|forecast_districts|high_sea_areas|marine_zones|metros|ocean_wind_warning|point_places|radar_coverage|radar_location|rainfall_districts]
                                      choose a spatial type
      -f, --table-format [fancy_grid|grid|html|jira|latex|latex_booktabs|mediawiki|moinmoin|orgtbl|pipe|plain|psql|rst|simple|textile|tsv]
                                      choose a table type
      --help                          Show this message and exit.


Examples
========

.. code::

   $ bomshell spatial tabledump --spatial-type radar_coverage --table-format rst

Results in the following table:

================  ==========  ===========  ==========  =======================================  ============  =============  =======  =======================  =======  =========  =========
Name                RADAR_ID    LONGITUDE    LATITUDE  FULL_NAME                                IDRNN0NAME    IDRNN1NAME     STATE    TYPE                     GROUP    STATUS     ARCHIVE
================  ==========  ===========  ==========  =======================================  ============  =============  =======  =======================  =======  =========  =========
South Doodlakine          58      117.953    -31.777   South Doodlakine                         SthDood       SthDoodlakine  WA       Doppler                  Yes      Public     SthDood
Weipa                     18      141.925    -12.666   Weipa                                    Weipa         Weipa          QLD      Doppler                  Yes      Public     Weipa
Sydney                    71      151.209    -33.7008  Sydney (Terrey Hills)                    TerreyHills   TerreyHills    NSW      Doppler                  Yes      Public     T_Hills
Adelaide                  64      138.469    -34.6169  Adelaide (Buckland Park)                 BuckPk        BucklandPk     SA       Doppler                  Yes      Public     BuckPk
Alice Springs             25      133.888    -23.796   Alice Springs                            AliceSp       AliceSprings   NT       Part-time windfinding    Yes      Public     AliceSp
Brisbane                  66      153.24     -27.7178  Brisbane (Mt Stapylton)                  MtStapl       MtStapylton    QLD      Doppler                  Yes      Public     MtStapl
Broome                    17      122.235    -17.9483  Broome                                   Broome        Broome         WA       Part-time windfinding    Yes      Public     Broome
Cairns                    19      145.683    -16.817   Cairns                                   Cairns        Cairns         QLD      Doppler                  Yes      Public     Cairns
Carnarvon                  5      113.669    -24.8878  Carnarvon                                Carnvn        Carnarvon      WA       Dedicated weather watch  Yes      Public     Carnvn
Ceduna                    33      133.696    -32.1298  Ceduna                                   Ceduna        Ceduna         SA       Dedicated weather watch  Yes      Public     Ceduna
Dampier                   15      116.687    -20.65    Dampier                                  Dampier       Dampier        WA       Dedicated weather watch  Yes      Public     Dampier
Darwin                    63      130.925    -12.457   Darwin (Berrimah)                        Berrima       Darwin         NT       Doppler                  Yes      Public     Berrima
Esperance                 32      121.892    -33.8303  Esperance                                Esprnce       Esperance      WA       Part-time windfinding    Yes      Public     Esprnce
Mt Gambier                14      140.775    -37.7477  Mount Gambier                            Gambier       MtGambier      SA       Dedicated weather watch  Yes      Public     Gambier
Geraldton                  6      114.697    -28.8044  Geraldton                                Gerlton       Geraldton      WA       Part-time windfinding    Yes      Public     Gerlton
Giles                     44      128.3      -25.03    Giles                                    Giles         Giles          WA       Part-time windfinding    Yes      Public     Giles
Gladstone                 23      151.263    -23.855   Gladstone                                Gladstn       Gladstone      QLD      Dedicated weather watch  Yes      Public     Gladstn
Gove                       9      136.823    -12.275   Gove                                     Gove          Gove           NT       Part-time windfinding    Yes      Public     Gove
Grafton                   28      152.951    -29.622   Grafton                                  Grafton       Grafton        NSW      Dedicated weather watch  Yes      Public     Grafton
Mornington Is             36      139.167    -16.666   Mornington Island (Gulf of Carpentaria)  GlfCarp       GulfCarp       NT       Dedicated weather watch  Yes      Public     GlfCarp
Halls Creek               39      127.663    -18.231   Halls Creek                              HallsCk       HallsCreek     WA       Part-time windfinding    Yes      Public     HallsCk
Port Hedland              16      118.632    -20.3719  Port Hedland                             PtHedland     PtHedland      WA       Dedicated weather watch  Yes      Public     P_Hedld
Hobart Ap                 37      147.501    -42.8374  Hobart Airport                           HobartAP      HobartAP       TAS      Part-time windfinding    Yes      Reg_users  HobrtAP
Gympie                     8      152.577    -25.9574  Gympie (Mount Kanigan)                   Kanign        Gympie         QLD      Doppler                  Yes      Public     Kanign
Kurnell                   54      151.226    -34.0148  Sydney (Kurnell)                         Kurnell       Kurnell        NSW      Doppler                  No       Reg_users  Kurnell
Melbourne                  2      144.755    -37.8552  Melbourne (Laverton)                     Melb          Melbourne      VIC      Doppler                  Yes      Public     Melb
Learmonth                 29      113.999    -22.103   Learmonth                                Lrmonth       Learmonth      WA       Dedicated weather watch  Yes      Public     Lrmonth
Newcastle                  4      152.025    -32.73    Newcastle                                LemnTre       Newcasle       NSW      Doppler                  Yes      Public     LemnTre
Wollongong                 3      150.875    -34.2625  Wollongong (Appin)                       Wollgng       Wollgng        NSW      Doppler                  Yes      Public     Wollgng
Longreach                 56      144.29     -23.43    Longreach                                Longrch       Longreach      QLD      Part-time windfinding    Yes      Public     Longrch
Mackay                    22      149.217    -21.117   Mackay                                   Mackay        Mackay         QLD      Dedicated weather watch  Yes      Public     Mackay
Marburg                   50      152.539    -27.608   Brisbane (Marburg)                       Marburg       Brisbane       QLD      Dedicated weather watch  Yes      Public     Marburg
Mildura                   30      142.086    -34.235   Mildura                                  Mildura       Mildura        VIC      Dedicated weather watch  Yes      Public     Mildura
Moree                     53      149.85     -29.5     Moree                                    Moree         Moree          NSW      Dedicated weather watch  Yes      Public     Moree
Perth Ap                  26      115.976    -31.9273  Perth Airport                            PrthAP        PerthAP        WA       Part-time windfinding    No       Reg_users  PrthAP
Sellicks Hill             46      138.5      -35.33    Adelaide (Sellicks Hill)                 Sellick       Adelaide       SA       Dedicated weather watch  Yes      Public     Sellick
Katherine                 42      132.446    -14.513   Katherine (Tindal)                       Tindal        Tindal         NT       Dedicated weather watch  Yes      Public     Tindal
Wagga Wagga               55      147.467    -35.167   Wagga Wagga                              Wagga         Wagga          NSW      Part-time windfinding    Yes      Public     Wagga
Willis Is                 41      149.965    -16.2874  Willis Island                            Willis        WillisIs       QLD      Part-time windfinding    Yes      Public     Willis
Woomera                   27      136.803    -31.157   Woomera                                  Woomera       Woomera        SA       Dedicated weather watch  Yes      Public     Woomera
NW Tasmania               52      145.579    -41.181   NW Tasmania (West Takone)                WTakone       NW-Tas         TAS      Dedicated weather watch  Yes      Public     WTakone
Wyndham                    7      128.119    -15.453   Wyndham                                  Wyndham       Wyndham        WA       Dedicated weather watch  Yes      Public     Wyndham
Yarrawonga                49      146.023    -36.0297  Yarrawonga                               NE-Vic        Yarrawonga     VIC      Doppler                  Yes      Public     NE_Vic
Canberra                  40      149.512    -35.6614  Canberra (Captains Flat)                 CapFlat       CaptFlat       NSW      Doppler                  Yes      Public     CapFlat
Norfolk Is                62      167.933    -29.033   Norfolk Island                           Norfolk       NorfolkIs      NSW      Part-time windfinding    Yes      Public     Norfolk
Bowen                     24      148.075    -19.886   Bowen                                    Bowen         Bowen          QLD      Dedicated weather watch  Yes      Public     Bowen
Warrego                   67      147.349    -26.44    Warrego                                  Warrego       Warrego        QLD      Dedicated weather watch  Yes      Public     Warrego
Bairnsdale                68      147.576    -37.8876  Bairnsdale                               Bnsdale       Bairnsdale     VIC      Dedicated weather watch  Yes      Public     Bnsdale
Darwin Ap                 10      130.892    -12.4247  Darwin Airport                           Darwin        DarwinAP       NT       Part-time windfinding    No       Reg_users  Darwin
Melbourne Ap              51      144.831    -37.6656  Melbourne Airport                        MelbnAP       TullaAP        VIC      Part-time windfinding    No       Reg_users  MelbnAP
Emerald                   72      148.239    -23.5498  Emerald                                  Emerald       Emerald        QLD      Doppler                  Yes      Public     Emerald
Perth                     70      115.867    -32.3917  Perth (Serpentine)                       Serptin       Serpentine     WA       Doppler                  Yes      Public     Serptin
Namoi                     69      150.192    -31.0236  Namoi (Blackjack Mountain)               Namoi         Namoi          NSW      Doppler                  Yes      Public     Namoi
Townsville                73      146.551    -19.4198  Townsville (Hervey Range)                HrvyRng       HrvyRng        QLD      Doppler                  Yes      Public     HrvyRng
Hobart                    76      147.806    -43.1122  Hobart (Mt Koonya)                       MtKoonya      MtKoonya       TAS      Doppler                  Yes      Public     Koonya
Albany                    31      117.816    -34.9418  Albany                                   Albany        Albany         WA       Part-time windfinding    Yes      Public     Albany
Mt Isa                    75      139.555    -20.7112  Mount Isa                                Mnt_Isa       Mnt_Isa        QLD      Doppler                  Yes      Public     Mnt_Isa
Warruwi                   77      133.38     -11.6485  Warruwi                                  Arafura       Arafura        NT       Doppler                  Yes      Public     Arafura
Kalgoorlie                48      121.455    -30.7834  Kalgoorlie                               K/grlie       Kalgoorlie     WA       Doppler                  Yes      Public     K/grlie
Newdegate                 38      119.009    -33.097   Newdegate                                Ndegate       Newdegate      WA       Doppler                  Yes      Public     Ndegate
================  ==========  ===========  ==========  =======================================  ============  =============  =======  =======================  =======  =========  =========



The spatial data type needs to specified when doing queries on the database.

.. code::

   bomshell spatial tabledump --spatial-type forecast_districts --table-format fancy_grid

   ╒═══════════╤═══════════╤════════════════════════════════════════╤══════════════╤══════════════════════════╕
   │ AAC       │   DIST_NO │ DIST_NAME                              │ STATE_CODE   │ GROUP_NAME               │
   ╞═══════════╪═══════════╪════════════════════════════════════════╪══════════════╪══════════════════════════╡
   │ NSW_PW001 │         1 │ Northern Rivers                        │ NSW          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ NSW_PW002 │         2 │ Mid North Coast                        │ NSW          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ NSW_PW003 │         3 │ Hunter                                 │ NSW          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ NT_PW009  │         9 │ Tanami                                 │ NT           │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW001 │         1 │ Peninsula                              │ QLD          │ Northern Districts       │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW002 │         2 │ Gulf Country                           │ QLD          │ Northern Districts       │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW003 │         3 │ Northern Goldfields and Upper Flinders │ QLD          │ Northern Districts       │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW004 │         4 │ North Tropical Coast and Tablelands    │ QLD          │ Northern Districts       │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW005 │         5 │ Herbert and Lower Burdekin             │ QLD          │ Northern Districts       │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW006 │         6 │ Central Coast and Whitsundays          │ QLD          │ Central Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW007 │         7 │ Capricornia                            │ QLD          │ Central Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW008 │         8 │ Central Highlands and Coalfields       │ QLD          │ Central Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW009 │         9 │ Central West                           │ QLD          │ Western Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW010 │        10 │ North West                             │ QLD          │ Western Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW011 │        11 │ Channel Country                        │ QLD          │ Western Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW012 │        12 │ Maranoa and Warrego                    │ QLD          │ Western Districts        │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW013 │        13 │ Darling Downs and Granite Belt         │ QLD          │ Southeast Districts      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW014 │        14 │ Wide Bay and Burnett                   │ QLD          │ Southeast Districts      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ QLD_PW015 │        15 │ Southeast Coast                        │ QLD          │ Southeast Districts      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ SA_PW001  │         1 │ Adelaide Metropolitan                  │ SA           │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ SA_PW002  │         2 │ Yorke Peninsula                        │ SA           │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ SA_PW003  │         3 │ Kangaroo Island                        │ SA           │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ SA_PW004  │         4 │ Upper South East                       │ SA           │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW001 │         1 │ Mallee                                 │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW002 │         2 │ Wimmera                                │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW003 │         3 │ Northern Country                       │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW004 │         4 │ North East                             │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW005 │         5 │ East Gippsland                         │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW006 │         6 │ West and South Gippsland               │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW007 │         7 │ Central                                │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW008 │         8 │ North Central                          │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ VIC_PW009 │         9 │ South West                             │ VIC          │                          │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW001  │         1 │ Kimberley                              │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW002  │         2 │ Pilbara                                │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW003  │         3 │ Gascoyne                               │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW004  │         4 │ Goldfields                             │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW005  │         5 │ Eucla                                  │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW006  │         6 │ North Interior                         │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW007  │         7 │ South Interior                         │ WA           │ Mining and Pastoral      │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW008  │         8 │ Central West                           │ WA           │ South West Land Division │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW009  │         9 │ Lower West                             │ WA           │ South West Land Division │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW010  │        10 │ South West                             │ WA           │ South West Land Division │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW011  │        11 │ South Coastal                          │ WA           │ South West Land Division │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW012  │        12 │ South East Coastal                     │ WA           │ South West Land Division │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW013  │        13 │ Great Southern                         │ WA           │ South West Land Division │
   ├───────────┼───────────┼────────────────────────────────────────┼──────────────┼──────────────────────────┤
   │ WA_PW014  │        14 │ Central Wheat Belt                     │ WA           │ South West Land Division │
   ╘═══════════╧═══════════╧════════════════════════════════════════╧══════════════╧══════════════════════════╛



Versioning
==========

Current version is 1.1.0
