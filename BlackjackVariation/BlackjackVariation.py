# BLACKJACK VARIATION - 1 PLAYER
# Game score will begin at 100, and the game will last for five rounds
# At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score 
# Player can choose to draw another card to try to get their round score closer to 21, or they can end the round 
# The player can draw as many cards as they want until they end the round or their round score exceeds 21.
# At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins 
# After the five rounds, the player is given their total score and the game is over.

# ---- CARD VALUES ----
# Ace = 1
# Face cards (Jacks, Queens, Kings) = 10

import random

#initialzing game variables
gameScore = 100
roundScore = 0
round = 1   # round number
deck = []   # cards per suit in deck
drawn = []  # cards drawn during game

# function to build card deck - 4 cards per suit
# need to use <<list>>.append(listValue) because list is empty and indices do not exist yet
# using indices will cause an "out of range" index error
def rebuild():
    for i in range(1, 14):
        deck.append(4)		
        
# DEBUGGING        
# for num in deck:
#     print(num)

# choosing random cards from deck
# input number of times a random card is drawn
# records which cards are drawn and sets point values
# removes card from deck for each card drawn
def drawCard(times):
    
    for i in range(1, (times + 1)):
        card = random.randint(1, 13)   # picking suit
        
        # insert different points based on card drawn
        # if a face card, set point value to 10
        if 9 < card < 14:    
            drawn.append(10)
            
            
        
        # for any other card, set value to card suit number
        else:
            drawn.append(card)

# NEED TO FIX!

# faceCards = { 11 : jack,
#     12 : queen,
#     13 : king,
# }

# def jack():
#     print("You drew a jack.\n")
    
# def queen():
#     print("You drew a queen.\n")
    
# def king():
#     print("You drew a king.\n")    
    
# faceCardss[11]()                


# GAME STARTS - lasts for 5 rounds
while round < 6:
    
    # printing round number
    print("----- ROUND %d ------" % round)
    
    
        
    

