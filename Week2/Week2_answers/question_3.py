"""
Write a function named add_commas that accepts a string representing a number and returns a new string with a comma at every third position, starting from the right.

For example, the call of add_commas("12345678") returns "12,345,678".
"""


def main():

    def add_commas(number_str):
        
        # Initialize variables
        result = ""
        count = 0
        
        # Iterate through the characters of the number string in reverse order
        for char in reversed(number_str):
            count += 1
            result = char + result
            
            # Add a comma after every third digit (except for the last group)
            if count == 3 and len(number_str) > 3:
                result = "," + result
                count = 0
        
        return result

    # Example usage:
    number_str = "12345678"
    formatted_number = add_commas(number_str)
    print(formatted_number)  # Output: "12,345,678"





if __name__ == "__main__":
    main()
