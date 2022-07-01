from RegexPractice import *

menuValue = input("Enter 1 to show Regex Practice\nEnter 2 to show video regex\nEnter 0 to EXIT: ")

while(menuValue != 0):
    if(int(menuValue) == 1):
        regexAnwsers_self()
        menuValue = 0
    elif (int(menuValue) == 2):
        print("working")
        regexVideo()
        menuValue = 0
    elif(int(menuValue) == 0):
        print("Good bye")
        quit()
    else:
        print("Invalid input")
        menuValue = input("Enter 1 to show Regex Practice\nEnter 0 to EXIT\n: ")
