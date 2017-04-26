# PyPBE

![PyePBE](https://github.com/drericstrong/pypbe/blob/master/images/pypbe_small.jpg)

[![PyPI version](https://badge.fury.io/py/pypbe.svg)](https://badge.fury.io/py/pypbe)
[![Documentation Status](https://readthedocs.org/projects/pypbe/badge/?version=latest)](http://pypbe.readthedocs.io/en/latest/?badge=latest)

### Python Point Buy Equivalence Calculator

*Sarah, John, and Kara sit down to play the first session of a new Pathfinder campaign with their GM, Lee. Sarah is excited about playing her favorite class, a Ranger. It doesn't matter what stats she rolls- she'll make it work. John is a bit of a min-maxer and wants to roll up a Wizard, so he's keen on getting the highest intelligence possible. Kara wants to play a Monk, which requires decent stats in a few different attributes.* 

*Lee decides that he wants the players to randomly roll for their character's stats. Sarah is excited about the chance for high stats. She's feeling especially lucky today. John, however, is angry. What if he doesn't roll any 18s for his intelligence? Kara is worried. She really wants to play a Monk, but she wants the character to be effective, and bad rolls could significantly reduce the fun she'll have playing the character.*

*What should Lee do?*

PyPBE is a resource for tabletop gaming which allows Gamemasters (GM) to fairly select which random rolling method is closest to an equivalent Point Buy value. Ideally, all players will determine their character's stats exactly the same way. However, in some cases (as in the story above), players may ask for several different options for generating their character's stats. PyPBE is designed to allow GMs to make this decision in a fair way.

As you work with PyPBE, you might also become concerned about the high variance inherent with every one of these methods and decide that you don't ever want random rolling in your game.

## Overview
Some GMs prefer to let their players choose between rolling for their ability scores and letting them use the Point Buy system. However, not all random rolling methods are created equal. Some (4d6, drop lowest) clearly give higher average results than others (3d6). PyPBE is designed to calculate and visualize the distribution of a specified ability score rolling method, which may provide useful information for decision-making.

The stats that PyPBE calculates aren't the "raw" values of the roll (e.g. typically 3 through 18), they're the "Point Buy Equivalent" of 6 rolls using that rolling method. For instance, if you roll 3d6 six times, you might get 10, 12, 8, 13, 7, 9, which has a Point Buy Equivalent of -2 (0+2-2+3-4-1) using the Pathfinder point buy scheme. 

PyPBE uses Monte Carlo simulation to obtain its results. If you perform the above process thousands/millions of times, you will get a distribution. The mean of that distribution is the fair Point Buy you should select for that rolling method, and 90% of the time, the random roll PBE will fall between the 5%/95% values. The "Typical Array" gives the most likely stat array using that random rolling method.

## Systems
PyPBE is designed for Pathfinder, 3.5e, and 5e characters. However, it allows the option to supply a custom Point Buy mapping, which means that it is applicable for any system in which the "Point Buy" concept applies. PyPBE also supports any number of attributes, although it was designed for the common 6-attribute system (strength, constitution, dexterity, intelligence, wisdom, charisma).

## Documentation
Current documentation can be found [here](https://pypbe.readthedocs.io/en/latest/).

## Getting Started
When using PyPBE as a Python module, the following dependencies are required:

**numpy, seaborn, matplotlib**

PyPBE can be installed using pip:

**pip install pypbe**

## Examples
Import the PBE class into your program, initializing it using the number and type of dice to roll, then use the "roll_mc" method to investigate the distribution. The results can be visualized using the "plot_histogram" method, and a data row summary can be generated using the "get_results" method. 

For example, running a simulation for three 6-sided dice (3d6), rolled for 6 attributes, can be accomplished using the following code:

> from pypbe import PBE

> alg = PBE(3,6)

> alg.roll_mc()

> alg.plot_histogram()

> results = alg.get_results()

The "plot_histogram" function will generate a plot that looks like this:

![Example Histogram](https://github.com/drericstrong/pypbe/blob/master/images/4d6_example.png)

The top part of the plot shows the distribution of each dice roll, ranked from lowest (Roll 1) to highest (usually Roll 6). Think about it this way- the mean value of 6 sets of 3d6, repeated many times, will tend towards 10.5 (each six-sided dice has a mean of 3.5, so 3.5 times 3 equals 10.5). However, if you order the 6 sets from lowest to highest, you'll notice that the lowest roll tends to be lower than 10.5, and the highest roll tends to be higher than 10.5. The plot shows the expected value for each ranked roll, which can be interpreted as the "typical" stat array for this rolling method. The 5th and 95th percentiles are given in brackets. For instance, [5,11] means that 90% of the distribution is between 5 and 11.

The distribution of the Point Buy value is shown in the bottom plot by mapping the results of each dice roll to a Point Buy value. The default mapping is: {3:-16, 4:-12, 5:-9, 6:-6, 7:-4, 8:-2, 9:-1, 10:0, 11:1, 12:2, 13:3, 14:5, 15:7, 16:10, 17:13, 18:17}. The mean, standard deviation, 5th, and 95th percentiles are shown on the figure. You can interpret the mean of the Point Buy distribution as the "Point Buy Equivalent"- the Point Buy value that is most fair to choose as the equivalent for the ability score rolling method.

The "roll_mc" and "plot_histogram" methods can be chained, like this:

> results = alg.roll_mc().plot_histogram().get_results()

## Custom Parameters
More complicated scenarios can be run by adjusting the following user-specified parameters:

* **add_val**: The value to add to the dice roll. (i.e. this is the "8" in "1d10+8")
* **num_ability**: The number of ability scores to generate. Default is 6 ability scores.
* **num_arrays**: The number of ability scores arrays that can be chosen from. For instance, 2 arrays might allow the player to choose between [12,10,6,11,15,17] and [6,9,12,18,15,10]
* **reroll**: Allow dice re-rolling, cumulatively. "0" is no re-rolls, "1" is re-rolling 1s, and "2" is re-rolling 1s and 2s, and so on.
* **best_dice**: If you want to roll more dice than you need and then take the best N results. E.g. "Roll 4d6 and drop the lowest roll" would require a "3" here.
* **best_ability**: If you want to roll more abilities than you need and then take the best N results. E.g. "Roll 3d6 seven times, and take the best six times" would require a "6" here. Must be less than or equal to num_ability.
* **pbe_map**: This determines how much each ability score will "cost" in the Point Buy system. You supply a string here, and the default is Pathfinder. You can (currently) select Pathfinder: 'pf', D&D 3e: '3e', D&D 4e: '4e', or D&D 5e: '5e'

For instance, running a simulation for 2d6+6, with the best 6 out of 7 ability scores, rerolling 1s, and choosing from 3 arrays, should be initialized like this:

> alg = PBE(2, 6, add_val=6, num_ability=7, best_ability=6, reroll=1, num_arrays=3)


