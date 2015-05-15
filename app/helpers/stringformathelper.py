# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

def matches(item, source):
    """Checks whether to strings have the same format.
    For instance, the strings 'ab23?' would be deemed to match 'qp82!', whereas 'abc' and '123' are not mathching."""
    # If they aren't the same length, they cannot be equal.
    if len(item) != len(source):
        return False

    # If a match is found, it goes to the next character.
    for i in range(0, len(source)):
        # Checks if the characters both are either '{' or '}'.
        if (item[i] is '{' or item[i] is '}') and item[i] is not source[i]:
            return False
        # Checks if both characters are digits
        if item[i].isdigit() and source[i].isdigit():
            continue
        # Checks if both characters are numbers
        if item[i].isalpha() and source[i].isalpha():
            continue
        # Checks if neither of the characters are numbers or letters, making them a character.
        if not (item[i].isdigit() or item[i].isalpha()) and not (source[i].isdigit() or source[i].isalpha()):
            continue

        # If none of the above passed, the sequence isn't matching.
        return False

    # If all the characters were matching, it's obviously matching.
    return True

print(matches('{', '}'))
print('{' is '}')
print(('{' is '{' or '{' is '}') and '{' is '}')
