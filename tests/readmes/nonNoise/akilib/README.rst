=========================================================
Python Hardware Library
=========================================================


This Library is Hardware Library. and You can buy parts in Japan Akihabara .

このライブラリは、秋葉原で購入出来る部品を使いやすくライブラリ化しました。

Akihabara Library =>  akilib

秋葉原で購入出来るライブラリ = akilib


1.Install
-------------------------------------------------------------------------------------------------------------

- Edison

    > opkg install python-pip

    > pip install pip --upgrade

    > pip install akilib

- RaspberryPi

    > sudo apt-get install python-pip

    > sudo pip install pip --upgrade

    > sudo pip install akilib



1.Library
-------------------------------------------------------------------------------------------------------------

- Edison
    - HDC1000       [ `AKI_I2C_HDC1000`_ ]
    - L3GD20        [ AKI_I2C_L3GD20 ]
    - LPS25H        [ `AKI_I2C_LPS25H`_ ]
    - LIS3DH        [ AKI_I2C_LIS3DH ]
    - MCP23017      [ AKI_I2C_MCP23017 ]
    - SO1602AWYB    [ AKI_I2C_SO1602AWYB ]
    - S11059        [ AKI_I2C_S11059 ]
    - AQM0802A      [ AKI_I2C_AQM0802A ]
    - AQM1248A      [ AKI_SPI_AQM1248A ]
    - SG12864ASLB   [ AKI_GPIO_SG12864ASLB ]

- RaspberryPi
    - AQM1602A      [ AKI_I2C_AQM1602A ]
    - HDC1000       [ `AKI_I2C_HDC1000`_ ]
    - LPS25H        [ `AKI_I2C_LPS25H`_ ]
    - ADT7410       [ AKI_I2C_ADT7410 ]
    - S11059        [ AKI_I2C_S11059 ] **NEW**

2.License
-------------------------------------------------------------------------------------------------------------

    The MIT License (MIT)
    Copyright (c) 2015 Yuta KItagami (kitagami@artifactnoise.com,@nonnoise)


.. _`AKI_I2C_HDC1000`: https://github.com/nonNoise/akilib/blob/beta/document/AKI_I2C_HDC1000.rst
.. _`AKI_I2C_LPS25H`: https://github.com/nonNoise/akilib/blob/beta/document/AKI_I2C_LPS25H.rst
