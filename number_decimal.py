#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : November 2019
# This program round a number


import math


def round_num(mlist):
    # Process
    mlist[2] = mlist[0] * pow(10, mlist[1])
    mlist[2] = mlist[2] + 0.5
    mlist[0] = mlist[2] / pow(10, mlist[1])


def main():
    # This function gets the input and passes it to another function

    # Input
    mylist = []
    number = input("What number do you want to round? ")
    times = input("Which decimal do you want to round? ")
    result = None
    try:
        number = float(number)
        times = int(times)
    except(Exception):
        print("Invalid input!")
        return
    if number <= 0 or times <= 0:
        print("Number must be more than 0!")
        return
    extra = 0
    mylist.append(number)
    mylist.append(times)
    mylist.append(result)
    mylist.append(extra)

    # Passing to another funtion
    round_num(mylist)

    # Output
    print("The rounded number is {0}".format(mylist[0]))


if __name__ == "__main__":
    main()
