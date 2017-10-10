# Dice Rolling Python Project - Charles Joseph Monaghan 11/10/2017

# Useful module for selecting random numbers
import random

# Loop program back to here once user presses anything
loop = 1
while (loop < 10):

    # Chooses random number between 1 - 6
    Random_Number = (random.choice([1, 2, 3, 4, 5, 6]))

    #Printing what the user sees
    print ("===============================")
    print ("Your random dice number is:", Random_Number)
    input("Press any key to roll again")
    print ("===============================")

    #looping back to "loop = 1"
    loop = loop + 1
