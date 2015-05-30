# COUNTDOWN CLOCK
# User to inputs time and date
# Program will print out a message at given intervals, telling user how much longer there is until the selected time

# SUBGOALS
# If the selected time has already passed, have the program tell the user to start over.
# Asks for the year, month, day, hour separately, allow the user to type in either the month name or its number.
# Use of built in modules such as time and datetime can change this project from a nightmare into a much simpler task.

import time
import datetime

# DEBUGGING FUNCTION
def debug(list):
    for item in list:
        print(item)
    return

# executes and prints countdown
def countdown():
    return

# gets datetime from user for countdown
def get_datetime():
    ask = ["Month ", "Day", "Year", "Hour", "Minute"]  # list containing strings to fill in the input statement
    datetime = []   # datetime list

    print("Enter the starting date and/or time for your countdown...")
    for word in ask:
        ans = input("%s: " % word)
        datetime.append(ans)

    debug(datetime)
    return

# main function
# executes get_datetime function
def main():
    get_datetime()
    return

# calls main function
if __name__ == "__main__":
    main()
