# PYTHAGOREAN TRIPLE CHECKER
# User enters values for the length of each side of a triangle
# Checker will output whether or not the triangle is a pythagorean triple

while True:     # creates loop for program to restart continuously
    # asking user to enter the side lengths of the triangle
    print("Enter the lengths for each side of the triangle (must be integer).")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    # recursive euclidean algorithm to determine if GCD of the sides = 1
    # if so, the triangle is a pythagorean triple
    def euclidean(x, y):
        gcd = 0     # initializing gcd variable
        if x > y:
            xprime = x
            x = y
            y = xprime

        r = y % x
        # print("Initial r: %d" % r)  # DEBUGGING

        while r > 0:
            gcd = r
            # print("gcd: %d" % gcd)  # DEBUGGING
            r = x % r
            # print("r during calculations: %d" % r)  # DEBUGGING
        return gcd

    if euclidean(a, b) != 1:
        print("Your triangle is not a pythagorean triple.\n")

    elif euclidean(b, c) != 1:
        print("Your triangle is not a pythagorean triple.\n")

    elif euclidean(a, c) != 1:
        print("Your triangle is not a pythagorean triple.\n")

    else:
        print("Your triangle is a pythagorean triple!\n")


