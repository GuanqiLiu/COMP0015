"""
Write a function named is_rotation that accepts two strings as parameters and returns true if they are rotations of each other. Two strings are considered rotations if they contain the same characters in the same relative order when wrapped around.

For example, the call of is_rotation("abcde", "deabc") should return True. The call of is_rotation("abcde", "edcba") should return False because the characters are not in the same order.

Note: a string is also considered to be its own rotation.
"""


def main():

    def is_rotation(str1, str2):
        # Check if the lengths of the strings are different
        if len(str1) != len(str2):
            return False

        # Double the first string to check for rotations
        str1 += str1

        # Check if str2 is a substring of the doubled str1
        if str2 in str1:
            return True

        return False

    # Example usage:
    string1 = "abcde" 
    string2 = "deabc"
    result = is_rotation(string1, string2)
    print(result)  # Output: True

    string3 = "abcde"
    string4 = "edcba"
    result = is_rotation(string3, string4)
    print(result)  # Output: False



if __name__ == "__main__":
    main()
