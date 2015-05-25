# TURN-BASED GAME
# User plays against computer, starting with 100 health points.
# Each move will serve one of three levels of damage:
# 1. Moderate damage with small range - reduces health by 18-25 points
# 2. High or Low damage with large range - reduces health by 10-35
# 3. Heal whoever casts the move by a moderate amount - increases caster's health by 18-25 points
# Game is over when either the computer or player reaches 0 health points

import random

def goes_first():
    print("Deciding if the computer of player will make the first move. Please wait...")
    p = random.random()     # randomly deciding if computer (0-0.5) or player (0.51-1.0) goes first

    # Computer goes first if p is between 0 and 0.5, inclusive
    if 0 <= p <= 0.5:
        lead = 1

    # Player goes first if p is between 0.5 and 1.0, inclusive
    elif 0.5 < p <= 1.0:
        lead = 2

    return lead

# executes moves
# takes in move choice, who casted the move, and the receiver of the move
def make_move(move, caster):
    # create turn list, stores damage/heal value and receiver of the move
    turn = []

    if move == 1:
        move_name = "Wind Fist"
        damage = random.randint(18, 25)     # random damage between 18-25 health points
        print("%s cast %s causing %d health points of damage.\n" % (caster, move_name, damage))

    elif move == 2:
        move_name = "Earth Kick"
        damage = random.randint(10, 35)     # random damage between 10-35 health points
        print("%s cast %s causing %d health points of damage.\n" % (caster, move_name, damage))

    elif move == 3:
        move_name = "Air Palm"
        damage = random.randint(18, 25)     # random heal to caster between 10-35 health points
        print("%s cast %s, healing by %d health points.\n" % (caster, move_name, damage))

    # add move choice and damage/heal value
    turn.append(move)
    turn.append(damage)
    return turn

# executes computer's move
# takes in computer's and player's health points
def computer(c_hp):
    # execute if computer health is between 0 and 35, inclusive
    # increased chance of healing move (move 3)
    if 0 < c_hp <= 35:
        r = random.random()  # choosing move based on modified distribution

        # execute Move 1 for r between 0 and 0.25, inclusive
        if 0 <= r <= 0.25:
            c_move = 1

        # execute Move 2 for r between 0.25 and 0.5, inclusive
        elif 0.25 < r <= 0.5:
            c_move = 2

        # execute Move 3 for r between 0.5 and 1.0, inclusive
        elif 0.5 < r <= 1.0:
            c_move = 3

    # computer in good health between 36 and 100 points, inclusive
    # choosing move randomly
    elif 35 < c_hp <= 100:
        c_move = random.randint(1, 3)

    move = make_move(c_move, "The Computer")
    return move

# takes user input and executes player's choice of move
# takes in computer's and player's health points
def player():
    p_move = int(input("Enter the move you'd like to make (1, 2, or 3): "))

    move = make_move(p_move, "You")
    return move

# updates health points for computer and player after move(s)
# takes in turn list, computer and player health points
def update(turn, c_hp, p_hp, cast_by):
    # create new health points list
    # index 0 for computer, index 1 for player
    health = []

    if turn[0] == 1 or turn[0] == 2:
        # if move was cast by computer
        # only updates to new value if health will not be negative, else sets health to zero
        if cast_by == 1:
            if (p_hp - turn[1]) >= 0:
                p_hp -= turn[1]
            else:
                p_hp = 0

        # if move was cast by player
        elif cast_by == 2:
            if (c_hp - turn[1]) >= 0:
                c_hp -= turn[1]
            else:
                c_hp = 0

    # only adds health points to reach max of 100 health points
    if turn[0] == 3:
        # if move was cast by computer
        if cast_by == 1:
            if (c_hp + turn[1]) <= 100:
                c_hp += turn[1]
            else:
                c_hp = 100

        # if move was cast by player
        elif cast_by == 2:
            if (p_hp + turn[1]) <= 100:
                p_hp += turn[1]
            else:
                p_hp = 100

    # adding updated stats to health list
    health.append(c_hp)     # index 0 = computer health
    health.append(p_hp)     # index 1 = player health
    return health

# prints health stats after each turn
def print_stats(c_hp, p_hp):
    print("----- STATS -----")
    print("Computer: %d" % c_hp)
    print("Player: %d\n\n" % p_hp)

    return

# calls game function
def main():
    # loop = True

    # resetting health points
    comp_hp = 100
    plyr_hp = 100

    # printing move choices for player
    print("---------- INTRO -----------\n")
    print("You can choose to make one of three possible moves:")
    print("1 - Wind Fist: Moderate damage, Low range")
    print("2 - Earth Kick: Low to High damage, High range")
    print("3 - Air Palm: Moderate healing, Low range\n")

    start = int(goes_first())

    # Computer makes the first move
    if start == 1:
        print("The COMPUTER will make the FIRST MOVE.\n")

        while 0 < comp_hp <= 100 and 0 < plyr_hp <= 100:
            # checking if computer health is zero
            if comp_hp > 0:
                # computer makes a move and health points are updated
                c_turn = computer(comp_hp)
                hp = update(c_turn, comp_hp, plyr_hp, 1)       # inputs cast_by as 1 = computer

                # updating and printing health stats
                comp_hp = hp[0]
                plyr_hp = hp[1]
                print_stats(comp_hp, plyr_hp)
            else:
                break

            # checking if player health is zero
            if plyr_hp > 0:
                # player makes a move and health points are updated
                p_turn = player()
                hp = update(p_turn, comp_hp, plyr_hp, 2)       # inputs cast_by as 2 = player

                # updating and printing health stats
                comp_hp = hp[0]
                plyr_hp = hp[1]
                print_stats(comp_hp, plyr_hp)
            else:
                break

    # Player makes the first move
    if start == 2:
        print("The PLAYER will make the FIRST MOVE.\n")

        while 0 < comp_hp <= 100 and 0 < plyr_hp <= 100:

            # checking if player health is zero
            if plyr_hp > 0:
                p_turn = player()
                hp = update(p_turn, comp_hp, plyr_hp, 2)       # inputs cast_by as 2 = player

                # updating and printing health stats
                comp_hp = hp[0]
                plyr_hp = hp[1]
                print_stats(comp_hp, plyr_hp)
            else:
                break

            # checking if computer health is zero
            if comp_hp > 0:
                # player makes a move and health points are updated
                c_turn = computer(comp_hp)
                hp = update(c_turn, comp_hp, plyr_hp, 1)       # inputs cast_by as 1 = computer

                # updating and printing health stats
                comp_hp = hp[0]
                plyr_hp = hp[1]
                print_stats(comp_hp, plyr_hp)
            else:
                break

    # printing winner
    if comp_hp == 0:
        print("The PLAYER wins!")
    elif plyr_hp == 0:
        print("The COMPUTER wins!")

    return

# calling main function
if __name__ == "__main__":
    main()
