"""
Write a function named remove_duplicates that accepts a string parameter and returns a new string with all consecutive occurrences of the same character in the string replaced by a single occurrence of that character.

For example, the call of remove_duplicates("bookkeeeeeper") should return "bokeper".
"""


def main():

    def remove_duplicates(input_str):

        # Initialize the result string with the first character
        result = input_str[0]

        # Iterate through the string, appending only non-consecutive duplicates to the result
        for i in range(1, len(input_str)):
            if input_str[i] != input_str[i - 1]:
                result += input_str[i]

        return result

    # Example usage:
    input_str = "bookkeeeeeper"
    result_str = remove_duplicates(input_str)
    print(result_str)  # Output: "bokeper"



if __name__ == "__main__":
    main()
