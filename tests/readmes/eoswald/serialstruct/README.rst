===================================
serialstruct  |build-status| |pypi|
===================================

Implements a StructuredPacket for pySerial's `serial.threaded` module

Installation
============
.. code-block:: bash

        $ pip install serialstruct


Motivation
==========
When sending a structured binary packet over Serial, the only way (that I'm aware
of) to guarantee packet alignment with arbitrary data is to send a header that's
larger than any of the elements and add padding between each element. Here's an
example:

.. code-block:: c

        struct Packet {
                int sensor1;
                int sensor2;
        }

If we send this over the wire and start reading at an arbitrary time, it's
impossible to know what byte of the packet we're reading. To mitigate this we can
add a header and some padding.

.. code-block:: c

        struct Packet {
                char header[5]; // Any sequence without a '\0'
                int sensor1;
                char pad1;      // '\0'
                int sensor2;
                char pad2;      // '\0'
        }

Now we just need to wait until the header sequence is read and we can consume the
rest of the packet without worrying about alignment.

pySerial only implements a FramedPacket which expects a unicode sequence that
starts with a '(' (0x28) and ends with a ')' (0x29). This means the bytes 0x28 and
0x29 cannot appear anywhere in the binary data.

Usage
=====
Subclass ``serialstruct.StructuredPacket`` to specify the data size in the packet
and to implement the ``handle_packet()`` callback function.

.. code-block:: python

        import struct

        import serial
        import serialstruct
        import time


        PACKET_STRUCT = struct.Struct("<IxIx")

        class MyPacket(serialstruct.StructuredPacket):

            DATA_SIZE = 10 # Excluding header: 4+1+4+1

            def __init__(self):
                super(MyPacket, self).__init__(self.DATA_SIZE)

            def handle_packet(self, packet):
                print(PACKET_STRUCT.unpack(packet))

            def send_packet(self, packet):
                self.transport.write(self.HEADER)
                self.transport.write(packet)


        ser = serial.serial_for_url("loop://", baudrate=115200, timeout=1)
        with serial.threaded.ReaderThread(ser, MyPacket) as protocol:
            # unsigned int, pad, unsigned int, pad; with no alignment
            packet = PACKET_STRUCT.pack(1, 2)
            protocol.send_packet(packet)
            time.sleep(1)

Prints:

.. code-block:: bash

        (1, 2)

.. |build-status| image:: https://travis-ci.org/eoswald/serialstruct.svg?branch=master
.. |pypi| image:: https://img.shields.io/pypi/v/serialstruct.svg?style=flat-square&label=latest%20stable%20version
    :target: https://pypi.python.org/pypi/serialstruct
    :alt: Latest version released on PyPi
