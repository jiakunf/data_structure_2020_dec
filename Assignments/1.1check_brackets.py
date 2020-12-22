# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
            # Process closing bracket, write your code here
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
