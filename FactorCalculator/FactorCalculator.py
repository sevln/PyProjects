# FACTOR CALCULATOR
# Asks user to input positive integer
# Calculates and prints out the factors of the integer in order from lowest to highest

import math

# calculates and prints out factors of integer input by user
# factors will always include 1 and the integer
# n = integer input by user

# DEBUGGING FUNCTION
def debug(my_list):
    for item in my_list:
        print(item)

def factor(n):
    lim = math.floor(math.sqrt(n))      # finding max whole number needed to find all factors
    # print("lim: %d " % lim)      # DEBUGGING

    # finding factors
    fact1 = [1]  # for small half of factors, including 1
    fact2 = [n]  # for large half of factors, including n

    # iterate through possible factors, starting at 2
    for i in range(2, lim + 1, 1):
        # print("i: %d" % i)    # DEBUGGING

        if n % i == 0:
            x = int(n / i)      # calculating second factor value

            fact1.append(i)     # adding small factor to first list
            # debug(fact1)    # DEBUGGING

            if x != i:          # adding large factor only if not a square factor
                fact2.append(x)
                # debug(fact2)      # DEBUGGING

    str1 = ','.join(str(f) for f in fact1)
    str2 = ','.join(str(f) for f in reversed(fact2))
    print(str1 + "," + str2)
    print("\n")
    return

# main function asks user to input integer for factoring
# calls factor function and outputs factors of integer input by user
def main():
    loop = True

    # continuous looping of program
    while loop:
        num = int(input("Enter a positive integer you'd like factored: "))        # asks user for integer to factor
        factor(num)     # factoring number entered by user

# calling main function
if __name__ == "__main__":
    main()
