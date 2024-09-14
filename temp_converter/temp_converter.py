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
#    return (c * 9 / 5) + 32 #Celsius is inputted and Farenheit is the output.
def f2c_raw(f):
    return (f - 32 * 5) / 9 #Farenheit is the input, and Celsius is the output. 

def f2c_op(f):
    return (f - 32 * 5) / 9

def main():
    f = 0           # input, setting the base value for Farenheit.
    c = f2c(f)      # Celsius is equal to the conversion of Farenheit to Celsius.
    print(f"{f}F is {c} C")

if __name__ == "__main__":
    main()


