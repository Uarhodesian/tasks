# 9.Define a function, which takes a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order.
#   Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
#   Examples:
#   []        OK   ][        NOT OK
#   [][]      OK   ][][      NOT OK
#   [[][]]    OK   []][[]    NOT OK

import re


def brackets():
    bracket_string = input("Enter random string with opening/closing brackets [ or ] : ")
    print("Your string", bracket_string)
    result = 0
    # Remove all found pairs of brackets using regex
    while len(re.findall(r'\[\]', bracket_string)) > 0:
        result = re.sub(r'\[\]', '', bracket_string)

        # If after removing all pairs of brackets the string is still not empty
        if len(result) > 0:
            print (bracket_string, 'NOT OK')
            break
        else:
            print (bracket_string, 'OK')
            break
