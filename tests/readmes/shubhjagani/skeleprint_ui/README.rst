SkelePrint UI - G Code Generator
########################################

The SkelePrint user interface allows you to generate g code for the SkelePrint 3D printer.  


.. class:: no-web

    .. image:: https://github.com/shubhjagani/skeleprint_ui/blob/master/screen_shot.png
        :alt: SkelePrint UI
        :width: 100%
        :align: center


.. class:: no-web no-pdf

.. contents::

.. section-numbering::
    



Installation
============


Installing Python
------------------


SkelePrint UI relies on python for processing. If you already have Python installed, you can skip ahead to the next step. 

**Mac OSX:**

.. code-block:: bash
    sudo brew install python

You may be asked to enter your password.

If you do not have homebrew installed, open up terminal and type:

.. code-block:: bash
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Installing homebrew may take a few minutes.


**Windows:**

Download and install the Python IDE using the link below:

`Python IDE`_


Installing pip
--------------

Download and save `get-pip.py`_ into any folder 

Open up Python IDE or Terminal, cd into the folder with the downloaded file and run the following command:

.. code-block:: bash

    cd ./Downloads/ 

    sudo python get-pip.py

You can also open the get-pip.py using Python IDE and run the script  


Installing SkelePrint UI
------------------------

A universal installation method (that works on Windows, Mac OS X, Linux, …,
and always provides the latest version) is to use `pip`_. 

All you have to do now is open terminal or command prompt and type: 

.. code-block:: bash
    # Make sure we have an up-to-date version of pip and setuptools:
    
    pip install --upgrade skeleprint_ui


Running SkelePrint UI
----------------------

After having successfully installed skeleprint_ui package simply open up terminal or command prompt and type:

.. code-block:: bash

    python

    import skeleprint_ui

A shortcut will be created on your desktop with the filename : SkelePrint_UI.pyc.

If you set this file to open with a Python IDE, you can now just open this file to run the tool path generator GUI. 


Updating SkelePrint UI
----------------------

You can update your version of Skeleprint UI by opening terminal or command prompt and typing:

.. code-block:: bash
    pip install --upgrade skeleprint_ui

Make sure you are running on the newest version of the tool path generator by checking `git`_


Usage
=====

Axial Length
------------

The axial length (mm) is equal to the total length of the print. Usually that means it is the same as the axial length of the printbed (220 mm). This can be changed if you would like to print shorter or longer helixes. The maximum traversable distance on the axial axis is approximately 280 mm, although it is not recommended to max out the axial travel as it makes it much harder to remove the print. 

Printbed Diameter
-----------------

The printbed diameter (mm) is equal to the diameter of the mandrel (10 mm). This value is fairly constant, but may need to be modified if the mandrel is coated in something or if you are using a different mandrel.

Final Print Diameter
--------------------

The final print diameter (mm) is equal to the final diameter of the print you would like to produce including the diameter of the printbed. 

Based on the value provided for the final print diameter the algorithm checks how many layers to print using the following logic:

.. code-block:: python

    layers = ((final_diameter - printbed_diameter)*0.5)/(filament_width * smear_factor)
    if (layers < 1):
        layers = 1.0

Filament Width
--------------

The filament width (mm) is equal to the inner diameter of the needle tip used. You can lookup the inner diameter of the needle gauge size on `this table`_

Helix Angle
-----------

The helix angle (degrees) is angle of the helix on each layer. This value is used to determine how many start points are required for each layer. It is often not possible to print at the exact angle you specified as the the number of start point must be a whole number. The algorithm take the value provided for the helix angle and adjusts it slightly to ensure the number of start point is a whole number. 

Helix Angle Conditions:

The helix angle has to be between [0,90] degrees. 

If the angle entered is greater 90 degrees, it will be set to 90 degrees. This means that layers will consist of many (almost) straight lines and have many start points. 

If angle entered is less than 0 degrees, it will be set to 0 degrees. This means that layers will consist of a single helix printed as close together as possible.

Feedrate
--------

The feedrate (mm/min) is equal to the speed of movement based on flow rate of the extrusion system. 

This feedrate should be calculated in the lab as follows:

flow rate = mL/s = cm^3/s

cross sectional area of nozzel = mm^2 

feed rate = flow rate/area = mm/s * 60  = mm/min

When this value is input into the GUI the algorithm uses it to calculate the tangential velocity using the folling algorithm:


.. code-block:: python

    hypotenuse = (math.pi * diameter) / math.cos(theta)
    time = hypotenuse/feedrate
    angular_velocity = (2 * math.pi)/time
    tangential_velocity = angular_velocity * (diameter/2) 

This value is re-calculated at each layer as the diameter changes at each layer.

Layer Height %
--------------

The layer height % is used to calculate the smear factor. At 100% the layer height is equal to the filament width. If layer height % is less than 100% then the radial axis only moves up some percentage of the filament width which means you are smearing the ink. 

I would take extra care when messing with this. 

Sending G Code to Printer
======================

Initalization
-------------

1. Make sure the axial axis and the radial axis limit switches are not triggered. If they are currently pressed, turn off the power supply. You will have to manually rotate the shaft to move the carriage away from the limit switch. Once you are a safe distance (at least 3mm) away you can continue. 

2. Make sure the power supply is connected to the printer. It's also a good idea at this point to check the wires and make sure everything is in place.

3. Turn on the power supply. At this points you might see some of the motors "kick" into place. This just means they are in closed loop mode. You can check that they are in closed loop mode by gently trying to rotate the motor, you should feel a lot of resistance. 

4. Now connect you computer to the Arduino Uno using the USB cable and open up the Universal GCode Sender (file name: UniversalGcodeSender.jar)

5. In the top left corner of the program, set Baud rate to 115200. Click the refresh button to right and make sure you are on the right usb port (you can also select it from the drop down list).

6. Now click open to open the connection to the Arduino which hosts the SkelePrint GRBL firmware. Once connected you should see a bunch of text in the console that starts with $1, $2 ... 

7. You should also see a red banner under the Machine Status section on the left hand side that says Active State: Alarm. That means that you have connected to the GRBL and it does not know where it is. 

NOTE: Axial Axis = X Axis, Rotational Axis = Y Axis, Radial Axis = Z Axis. 

8. Now we will home the printer. YOU MUST HOME THE PRINTER BEFORE EVERY USE. To home the printer, click into the "Command:" field and enter "$H" (without quotes). You can also just press the $H button near the top. The printer should start moving the axial axis toward the right hand side and perform the homing routine. 

9. If you want to continue from the current position without homing you can enter the command "$X" which will bypass the alarm set your current position as (0, 0, 0). But it is highly recommended that you home the printer every time you connect to it. 

NOTE: After homing is complete the positive x direction is left (<--) and the positive radial direction is set to up.

10. The axial axis is now homed. However you still need to manually calibrate the radial axis. You can do this by giving gcode commands such as "Z -10.3" (move down 10.3 mm), or using the direction button on the right hand side. Once you have calibrated the radial axis you need to set this position as 0 by clicking the "Reset Z Axis" button near the top (if you forget part it is okay because the gcode from the gcode generator will take care of it anyway).

11. You can now make any adjustments you need by giving direct gcode commands such as "X10 Y10 Z3.57" (move 10mm in the positive x direction, make one rotation of the printbed [10mm = 1 rotation], and move z-axis up 3.57 mm)

12. To start printing click browse under the "File" section on the left hand side and find the gcode you produced (should be saved on your desktop in a folder named "gcode"). When you are ready hit send to start printing! 

13. Hitting pause will pause the print and the gcode, but if you hit cancel you will lose your place. 


G Code Crash Course
-------------------

G0 - Linear move. This is used to move or job, not to print. Using a G0 command changes the work position so remember to reset your position after you have finished adjusting.

G1 - Linear move used to print. You can set the speed by setting the feedrate. "G1 F300" will move at 300 mm/min. Only need to define this once, any moves sent afterwards will move at previously defined feedrate. 

X, Y, Z - Move the respective axis. Used in congunction with G0 or G1 commands. "G1 F300 X10 Y30 Z4". If you give a move command without adding G1 it will make a G0 move. Ex. Sending "X120" is the same as sending "G0 X120".

M7 - Turn on UV laser. (currently not connected)

M8 - Start extruding. (currently not connected)

M9 - Stop all external machines. (Stop extruding + turn off UV laser).  

G10 P0 L20 X0 Y0 Z0 - Reset X, Y, Z axis coordinates to (0,0,0).

G21 - Set units to mm.

G90 - Set printer to operate in absolute distance mode.

G94 - Set units per minute feed rate mode.

$H - Start homing cycle.

$X - Bypass alarm.

$$ - View defaults.

More detailed info can be found here: https://www.shapeoko.com/wiki/index.php/G-Code

Supplementary Software
======================

You should download the entire supplementary software folder. It is home to all the source code for the GRBL firmware, the firmware and tuning software for the Mechaduino PCBs, and the G Code sender program which sends G Code to the Arduino.  



Meta
====

Interface design
----------------

The interface was designed using tkinter for Python. 


Authors
-------

`SkelePrint`_


.. _pip: https://pip.pypa.io/en/stable/installing/
.. _Python IDE: https://www.python.org/downloads/release/python-2713/
.. _git: https://github.com/shubhjagani/skeleprint_ui
.. _this table: http://www.sigmaaldrich.com/chemistry/stockroom-reagents/learning-center/technical-library/needle-gauge-chart.html
.. _get-pip.py: https://bootstrap.pypa.io/get-pip.py
.. _SkelePrint: http://skeleprint.ca




