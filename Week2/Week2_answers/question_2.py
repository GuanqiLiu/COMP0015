"""
Write a console program that prompts the user to type an integer and computes the sum of the digits of that integer. You may assume that the user types a non-negative integer. Match the following output format:

Type an integer: 827104
Digit sum is 22
"""


def main():
    # Prompt the user to enter an integer
    user_input = input("Type an integer: ")

    # Initialize the sum of digits to 0
    digit_sum = 0

    # Calculate the sum of digits
    for digit in user_input:
        digit_sum += int(digit)

    # Display the result
    print(f"Digit sum is {digit_sum}")



if __name__ == "__main__":
    main()
