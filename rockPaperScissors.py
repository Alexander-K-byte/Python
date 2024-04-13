import random
import re
from time import sleep
import sys

#random imported to allow cpu to choose an option
#regex used for input validation
#sys imported for exiting

#intro
print("Welcome to Rock, Paper, Scissors.\n")

#score counters
p = 0
c = 0

#run the game
while True:
    #take input from user
    p1 = input("Press Q to quit or choose a number\n"
          "1 = Rock, 2 = Paper, 3 = Scissors.\n").lower()
    #input validation single character
    if re.match("^[1|2|3|q]{1,1}$", p1):
        #if input is good, run randomiser for cpu
        cpu = str(random.randint(1,3))
        #if quit, break out while loop
        if p1 == "q":
            break
        #draw condition
        elif (p1 == cpu):
            print("Wow, a draw, no points awarded.")
        #win conditions
        elif (p1 == "1" and cpu == "3") or (p1 == "2" and cpu == "1") or (p1 == "3" and cpu == "2"):
            print("Player wins!\n")
            p += 1
            print("Player score: " + str(p) + " / CPU score: " + str(c) + "\n")
        #anything else is a loss
        else:
            print("CPU wins!\n")
            c += 1
            print("Player score: " + str(p) + " / CPU score: " + str(c) + "\n")
    #else for if input does not match regex
    else:
        p1 = print("Only acceptable inputs are....\n"
          "1 = Rock, 2 = Paper, 3 = Scissors, or q to quit\n")
#exit script and print final scores
sys.exit("Final scores:\nPlayer: " + str(p) + " CPU: " + str(c) + "\n"
    "GAME OVER MAN, GAME OVER!")

