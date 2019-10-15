#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: October 2019
# This is a program which tells you if your old enough to date this grandma's
# grandchild.

import constants


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what tells you if your old to date their grandchild.
    print("")
    print("Grandma: Oh! Your approaching me? Instead of running away, your "
          "coming right to me?")
    print('')

    while True:
        # Input
        age_as_string = input(color.BOLD + color.YELLOW + 'Input your age: '
                              + color.END)

        # Process
        try:
            age_of_user = int(age_as_string)
            if age_of_user >= constants.MINIMUM_AGE and \
               age_of_user <= constants.MAX_AGE:
                # Output
                print('')
                print('You: I cant date your grandchild'
                      ' without getting your approval.')
                print('')
                print(color.BOLD + color.GREEN + 'Grandma: Get my approval ' +
                      'then. I will gladly allow you to date my grandchild.' +
                      color.END)
                print('(You are old enough)')
                break
            # Process
            else:
                # Output
                print('')
                print('You: I cant date your grandchild'
                      ' without getting your approval.')
                print('')
                print(color.BOLD + color.RED + 'Grandma: Good grief... You' +
                      ' truly are the lowest scum in history...' +
                      color.END)
                print('(You arent old enough)')
                break
        # This stops them from putting in something let bob and gets them to
        # re-input their age.
        except Exception:
            print('')
            print(color.PURPLE +
                  'Grandma: Sorry... could you repeat that?' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
