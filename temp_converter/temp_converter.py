#!/usr/bin/python3
"""
temp.py - converts Celsius temperatures to Fahrenheit.
Name:    Cassidy Goss
Date:    20240905
Course Number:    138
Class Section:    EN
Changes:
    20240908 - Added Parenthesis, and comments.
    """
# process
def c2f(c):
    return (c * 9 / 5) + 32

def main(cel):
    return c2f(cel)
    
if __name__ == "__main__":
    cel =  100        # input
    print(main(cel))  # output
