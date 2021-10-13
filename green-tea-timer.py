#!/usr/bin/env python3

# welcomes the user and waits for the input to continue

print("Welcome to Green Tea Timer!\n\nLet's start brewing Green tea!")

# creates variables and instructions for varieties of green tea

green_instructions = "\nFor Green tea heat the water to 75-80C and let leaves steep for 1-2 minutes."

white_instructions = "\nFor White tea heat the water to 80-85C and let leaves steep for 2-3 minutes."

oolong_instructions = "\nFor Oolong tea heat the water to 80-90C and let leaves steep for 2-3 minutes."

puerh_instructions = "\nFor Pu-Erh tea heat the water to 90-95C and let leaves steep for 4-5 minutes."

#asks the user about which type of tea he wants to brew and serves up instructions accordingly

question = input("\nWhat type of Green tea  do you brew:\nGreen tea, White tea, Oolong tea or Pu-Erh tea?\n\n")

if question == ("Green tea"):
    print(green_instructions)
elif question == ("White tea"):
    print(white_instructions)
elif question == ("Oolong tea"):
    print(oolong_instructions)
elif question == ("Pu-Erh"):
    print(puerh_instructions)

input("\nPress enter when you are ready!\n")

# import the time module
import time

#define the countdown func
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:01d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("Enjoy your freshly steeped Green tea!")

# input time in seconds
if question == ("Green tea"):
    t = 120
elif question == ("White tea"):
    t = 180
elif question == ("Oolong tea"):
    t = 180
elif question == ("Pu-Erh tea"):
    t = 300

# function call
countdown(int(t))

# asks the user if they want to receive more information

question1 = input("\nDo you wish to receive more information about your Green tea? (y/n)")

# if user wants more information opens up wikipedia page

if question1 == ("y"):    
    import webbrowser
    if question == ("Green tea"):
        webbrowser.open("https://en.wikipedia.org/wiki/Green_tea")
        print("\nThank you very much for using Green Tea Timer and Goodbye!\n")
    elif question == ("White tea"):
        webbrowser.open("https://en.wikipedia.org/wiki/White_tea")
        print("\nThank you very much for using Green Tea Timer and Goodbye!\n")
    elif question == ("Oolong tea"):
        webbrowser.open("https://en.wikipedia.org/wiki/Oolong")
        print("\nThank you very much for using Green Tea Timer and Goodbye!\n")
    elif question == ("Pu-Erh tea"):
        webbrowser.open("https://en.wikipedia.org/wiki/Pu%27er_tea")
        print("\nThank you very much for using Green Tea Timer and Goodbye!\n")
elif question1 == ("n"):
    print("\nThank you very much for using Green Tea Timer and Goodbye!\n")