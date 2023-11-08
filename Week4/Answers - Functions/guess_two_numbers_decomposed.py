"""
Name: guess_two_numbers_decomposed.py

Description:

This program prompts the user for two numbers and checks whether they match two
randomly generated numbers.

Author: Rae Harbird
This problem was created by Rob Miller, DIS, UCL for a Java course.
"""

import random

# Prints message informing user guesses correct.


def output_yes():
    print("\tCorrect - well done!\n")

def output_no(answer_a, answer_b):
    """
    Checks the two guesses entered by the user against the two randomly generated numbers.
     @params answer_a the first answer
     @params answer_b the second answer
    """

    print("\tNo, the answers were {} and {}.\n".format(answer_a, answer_b))

def guesses_ok(answer_a, answer_b, guess_a, guess_b):
    """ 
    Checks the two guesses entered by the user against the two randomly generated numbers.
    @params answer_a the first answer
    @params answer_b the second answer
    @params guessA the first guess
    @params guessB the second guess
    @return True or False
    """

    ok_same_order = guess_a == answer_a and guess_b == answer_b
    ok_other_order = guess_a == answer_b and guess_b == answer_a
    return ok_same_order or ok_other_order


def main():
    min_ = 1
    max_ = 3
    
    first_answer = random.randrange(min_, max_ + 1)
    second_answer = random.randrange(min_, max_ + 1)
    
    first_guess = int(input("\n\tGuess the first number between {} and {}: ".format(min_, max_)))
    second_guess = int(input("\n\tGuess the second number between {} and {}: ".format(min_, max_)))

    if guesses_ok(first_answer, second_answer, first_guess, second_guess):
        output_yes()
    else:
        output_no(first_answer, second_answer)


# Start the program
if __name__ == "__main__":
    main()
