# CHANGE CALCULATOR - program that calculates change required in quarters, dimes, nickels, and pennies.
# 1. User inputs cost of item and amount paid
# 2. Program will output change required and the number of quarters, dimes, nickels, and pennies needed.

import math

loop = True

while loop:
    cost = float(input("Please enter the cost of the item: "))
    paid = float(input("Please enter the amount paid: "))

    while paid < cost:      # catches if amount is less than cost of item
        print('\nSorry, you still owe $%.2f! Please try again.' % (cost - paid))
        paid = float(input("\nPlease enter the amount paid: "))

    def calculate(c, p):
        diff = p - c
        if diff == 0:
            print('No change required.')
        else:
            q = math.floor(diff / 0.25)
            if diff % 0.25 > 0:
                diff -= 0.25 * q

                d = math.floor(diff / 0.1)
                if diff % 0.1 > 0:
                    diff -= 0.1 * d

                    n = math.floor(diff / 0.05)
                    if diff % 0.05 > 0:
                        diff -= 0.05 * n

                        p = math.floor(round(diff, 2) / 0.01)

                        # prints out change required and amount of each coin type to build the change
                        print('\nChange owing: $%.2f' % (paid - cost))
                        print('Requires: %d quarter(s), %d dime(s), %d nickel(s), and %d penny(ies).\n' % (q, d, n, p))


    calculate(cost, paid)
