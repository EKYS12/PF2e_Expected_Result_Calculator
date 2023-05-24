# PF2e Expected Value Calculator
This is a script that can calculate the expected value of a result from a check in PF2e. It takes in the DC of a check, the player modifier of the check, and the different value results for each tier of success and spits out the expected value of the roll. It also breaks down the probabilites of each success tier for the roll. 


## Future Goals
Currently the script only takes in constant values for the results. This means it works well for calculating something such as the expected value of an earn income roll by a player. But it doesn't currently work for results that have their own layer of randomness, like damage. Damage results are another set of dice rolls. Expanding the script to allow players to enter in their damage dice so that the script can tell them their expected damage, instead of themselves having to put in the expected damage per tier of success would be a great improvement.

Potentially make a simple web app for the script so that it isn't just run in a terminal.
