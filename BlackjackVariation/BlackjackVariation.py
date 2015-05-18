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

# initializing game variables
game_score = 100
round_score = 0
round_num = 1  # round number
deck = []  # cards per suit in deck
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


# GAME STARTS - lasts for 5 rounds
while round < 6:

    # printing round number
    print("----- ROUND %d ------\n\n" % round)

    # choosing random cards from deck
    # input number of times a random card is drawn
    # records which cards are drawn and sets point values
    # removes card from deck for each card drawn
    def draw_card(times):

        # tells player the face card drawn
        def face_card(n):
            if n == 11:
                print("You draw a JACK.\n")

            elif n == 12:
                print("You draw a QUEEN.\n")

            elif n == 13:
                print("You draw a KING.\n")

            # drawing card(s)
            for i in range(1, (times + 1)):
                print("You draw a card.\n")

                card = random.randint(1, 13)  # picking card value - the card drawn

                # checks if card value has cards left, else draws value again until a card can be drawn
                while deck[card] == 0:
                    card = random.randint(1, 13)

                deck[card] -= 1     # removing quantity left of card value drawn from deck

                # insert different points based on card drawn
                # if a face card, set point value to 10
                if 9 < card < 14:
                    drawn.append(10)
                    face_card(card)  # tell player which face card has been drawn

                # for any other card, set value to card suit number
                else:
                    drawn.append(card)
                    print("You draw a %d.\n" % card)

    draw_card(2)     # drawing two initial cards


    # checking card value scores to see if user has bust or can redraw
    def check_score():
        if sum(drawn) >= 21:  # if user has bust, round ends
            round += 1

        input("Draw again? (Y/N)")

    check_score()





