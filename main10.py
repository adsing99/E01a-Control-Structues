#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') # Prints out Greeting!
colors = ['red','orange','yellow','green','blue','violet','purple'] # A list named colors that has red, orange, yellow, green, blue, violet, and purple in it.
play_again = '' # A variable is created called play_again that is set to an empty string
best_count = sys.maxsize            # the biggest number 
while (play_again != 'n' and play_again != 'no'): # A while loop that only passes if play_again isn't n or no.
    match_color = random.choice(colors) # Sets the value of the match color for this round to a random color from the list colors
    count = 0 # Sets the count to 0
    color = '' #Sets the color to an empty string
    while (color != match_color): #A while loop that passes if the current color isn't the same as the match color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # formats the response to minimise the impact of capitalization and spacing
        count += 1 # increases the count by 1
        if (color == match_color): # If the color that was input is the same as the match color, this if statement passes
            print('Correct!') # Prints out Correct!
        else: # If the if statement didn't pass, the else case is activated
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #Prints out a response and sets guesses to count to tell the user how many times they have guessed so far.
    print('\nYou guessed it in {0} tries!'.format(count)) # Prints out a response that tells the user they got it and shows them how many tries it took.
    if (count < best_count): # Checks if the most recent game was lower then the previous best
        print('This was your best guess so far!') # If it was then let the user know
        best_count = count # Sets the new best count to be the score of the most recent game
    play_again = input("\nWould you like to play again? ").lower().strip() # Asks the user if they want to replay, taking in an input (presumably y or n)
print('Thanks for playing!') #Thanks the user for playing with a printed response