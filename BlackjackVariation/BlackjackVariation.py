# BLACKJACK VARIATION - 1 PLAYER
# Game score will begin at 100, and the game will last for five rounds
# At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the round score
# Player can choose to draw another card to try to get their round score closer to 21, or they can end the round
# The player can draw as many cards as they want until they end the round or their round score exceeds 21.
# At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins
# After the five rounds, the player is given their total score and the game is over.
# If player busts, 21 is subtracted from their total score.

# ---- CARD VALUES ----
# Ace = 1
# Face cards (Jacks, Queens, Kings) = 10

import random

# initializing game lists
deck = []  # cards per suit in deck
drawn = []  # cards drawn during game

# function to build card deck - 4 cards per suit
# need to use <<list>>.append(listValue) because list is empty and indices do not exist yet
# using indices will cause an "out of range" index error
def rebuild():
    for i in range(1, 14):
        deck.append(4)

# DEBUGGING FUNCTION
def print_deck():
    print("DECK:")
    for num in deck:
        print(num)
    print("\n")

# choosing random cards from deck
# input number of times a random card is drawn
# records which cards are drawn and sets point values
# removes card from deck for each card drawn
def draw_card(times):

    # tells player the face card drawn
    def face_card(n):
        if n == 11:
            print("It's a JACK.\n")

        elif n == 12:
            print("It's a QUEEN.\n")

        elif n == 13:
            print("It's a KING.\n")

    # drawing card(s)
    for i in range(1, (times + 1)):
        print("You draw a card.")

        card = random.randint(1, 13)  # picking card value - the card drawn
        # print(card)     # DEBUGGING

        # checks if card value has cards left, else draws value again until a card can be drawn
        if deck[card - 1] == 0:
            card = random.randint(1, 13)

        deck[card - 1] -= 1     # updating quantity left of card value drawn from deck

        # insert different points based on card drawn
        # if a face card, set point value to 10
        if 10 < card < 14:
            drawn.append(10)
            face_card(card)  # tell player which face card has been drawn

        # for any other card, set value to card suit number
        else:
            drawn.append(card)
            print("It's a %d.\n" % card)

        # print_deck()        # DEBUGGING

# checking card value scores to see if user has bust or can redraw
def check_score():
    total = sum(drawn)

    if total > 21:  # if user has bust, round ends
        print("Oh no. You have bust!\n")

    # if user hasn't bust, they can choose to draw another card
    else:
        print("Your current round score is: %d" % total)
        ans = str.lower(input("Draw again? (Y/N): "))
        print("\n")

        if ans == 'y':
            draw_card(1)
            check_score()

    return sum(drawn)       # returns updated card value total after redraws

# main function
def main():
    # initializing game variables
    game_score = 100
    round_num = 1  # initializing round number

    rebuild()   # rebuilding deck at start of game

    while round_num < 6:    # game lasts for 5 rounds
        print("----- ROUND %d -----\n\n" % round_num)     # printing round number
        round_score = 0     # resetting round score

        draw_card(2)     # drawing two initial cards

        round_score = check_score()

        if round_score > 21:  # checking user score and round status
            game_score -= 21    # getting game score
            print("|SCORES|\nRound Score: 21\nGame Score: %d\n" % game_score)

        elif round_score <= 21:
            game_score -= (21 - round_score)  # getting game score
            print("You decide not to draw any more cards.\n")
            print("|SCORES|\nRound Score: %d\nGame Score: %d\n" % (round_score, game_score))

        round_num += 1  # go to next round

        drawn[:] = []       # clears cards drawn

        if round_num == 5:
            print("Let's move onto the final round.\n\n")
            continue
        elif 0 < round_num < 5:
            print("Let's move onto the next round.\n\n")
            continue

    print("----- GAME OVER -----\nFINAL SCORE: %d" % game_score)

# calling main() function
if __name__ == "__main__":
    main()
