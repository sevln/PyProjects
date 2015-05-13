# HIGH-LOW GAME
# 1. Computer selects random integer between 1-100 (inclusive)
# 2. User must guess the integer, with hints from computer asking user to guess higher or lower

import random
game = True 
playing = True

while game:
    
    # computer selects random integer between 1-100, inclusive
    num = random.randint(1, 100)
    
    tries = 0

    invalid = True
    
    while playing:

        guess = int(input("Please guess an integer between 1-100, inclusive. Enter 0 to quit.: "))

            # def validate_input(input):
            #     try:
            #         g = int(input)
            #     except ValueError:
            #         print("The value you entered is not an integer. Please try again.")
            #     continue
            #     if 0 < g < 101:
            #         break;    
            #     else:
            #         print("The value you entered is not between 1-100. Please try again.")    


            # validate_input(guess)

            # player wants to exit game
        if guess == 0:  
            print("\nGoodbye. Thanks for playing!")
            quit()
        
        tries += 1
        
        def check(g, n):    
            
            if g == n:
                print("Congratulations! You guessed correctly in %d tries!\n" % tries)
        
            elif g > n:
                print("Guess a lower number!\n")
                
            elif g < n:
                print("Guess a higher number!\n")
                
        check(guess, num)