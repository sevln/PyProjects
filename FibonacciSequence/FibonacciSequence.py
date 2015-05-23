# FIBONACCI SEQUENCE
# Asks user to input desired term of Fibonacci sequence for program to return

# returns nth term of Fibonacci sequence
# n is input by user
def fib(num):
    # returns nth term of Fibonacci sequence
    # Term 0 = 0, Term 1 = 1, Term 2 = 0 + 1 = 1, etc
    # starting with n1 = 0, n2 = 1, term = 1

    n1 = 0
    n2 = 1

    # finding nth term based on user input
    for term in range(1, num, 1):
        total = n1 + n2
        # print(total)        # DEBUGGING

        n1 = n2
        # print(n1)        # DEBUGGING

        n2 = total
        # print(n2)        # DEBUGGING

    return total

# calls fib function
def main():
    loop = True

    # continuous looping of program
    while loop:
        # asking user to input desired term in Fibonacci sequence
        n = int(input("Enter the term in the Fibonacci sequence you would like returned: "))

        val = fib(n)
        print("Term #%d in the Fibonacci sequence is: %d\n" % (n, val))

# calling main function
if __name__ == "__main__":
    main()