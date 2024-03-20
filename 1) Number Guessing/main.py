import random
import math

#Taking Lower and Upper Bound from User as Input
lowerBound = int(input("Enter the Lower Bound: "))
upperBound = int(input("Enter the Upper Bound: "))

try:
    #Checking entered number is positive or not
    if  lowerBound < 0  or upperBound < 0:
        print("Enter Positive Numbers!!")
        raise ValueError("Error")
        
    #Checking wheather upper bound is greater than lower bound or not
    if lowerBound >= upperBound:
        print("UpperBound Should be greater than LowerBound!")
        raise ValueError("Error")

    #Generating random number between Lower and Upper Bound
    number = random.randint(lowerBound,upperBound)

    #implementing logic for Calculating Minimum Number of Guesses
    print("\n\tYou've only ",round(math.log(upperBound-lowerBound+1,2))," chances to guess the Number!\n")

    #Intializing number of Guesses
    count = 0
    luck = True
    #Code for Guessing number until Found or Guesses completed
    while count< round(math.log(upperBound-lowerBound+1,2)) :
        #Incrementing count for every Guess
        count+=1

        #Taking input for Guess
        guess = int(input("Guess the Number: "))

        #Checking the guessed Number
        if number == guess:
            print("\tCongratulations you did it in ",count," try")
            luck = False
            #If number guessed is correct break the loop
            break
        elif number > guess:
            print("You guessed too small!\n")
        elif number < guess:
            print("You Guessed too high!\n")
            
    # If Guessing is more than required guesses,
    # shows this output.
    if luck:
        print("\nThe number is %d" % number)
        print("\tBetter Luck Next time!")


except:
    print("Retry!!")