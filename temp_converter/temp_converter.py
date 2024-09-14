#!/usr/bin/python3
"""
temp.py - converts Celsius temperatures to Fahrenheit.
Name:    Cassidy Goss
Date:    20240905
Course Number:    138
Class Section:    EN
    """
# process
#def c2f(c):
#    return c * 9 / 5 + 32
def f2c_raw(f):
    return f - 32 * 5 / 9

def f2c_op(f):
    return (f - 32) * 5 / 9

def main():
    f = 0           # input
    c = f2c(f)
    print(f"{f}F is {c} C")

if __name__ == "__main__":
    main()


