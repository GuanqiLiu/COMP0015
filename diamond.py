"""
Name: pyramid.py

Description:

This program prompts the user for the height of a pyramid and prints it.

"""

MARGIN = 10

def pyramid_line(symbol, line_number, height):
    """ Construct string representing a line of the pyramid
    @param    symbol the symbol from which the pyramid will be printed
    @param    lineNumber the lineNumber in the pyramid
    @param    height the height of the pyramid
    @return   line the string representing a line of the pyramid
    """
    line = ""
    line += spaces_for_pyramid_line(line_number, height)
    line += symbols_for_pyramid_line(symbol, line_number)
    line += "\n"
    return line

def symbols_for_pyramid_line(symbol, line_num):
    """
    Construct string representing the symbols for a line of the pyramid
    # @param    symbol the symbol from which the pyramid will be printed
    # @param    lineNum the number of the line
    # @return   lineSymbols the string representing the symbols in a line of the pyramid
    """
    line_symbols = ""
    for symbols_count in range((line_num * 2) - 1):
        line_symbols += symbol
    return line_symbols

def spaces_for_pyramid_line(line_num, height):
    """
    Construct string representing the spaces for a line of the pyramid
    @param    lineNum the number of the line
    @param    height the height of the pyramid
    @return   lineSpaces the string representing the spaces in a line of the pyramid
    """
    line_spaces = ""
    for spaces_count in range(MARGIN + height + 1 - line_num):
        line_spaces += " "
    return line_spaces

def pyramid_string(character, height):
    """
    Construct string representing the pyramid
    @param    character the symbol from which the pyramid will be printed
    @param    height the height of the pyramid
    @return the string representing the pyramid
    """
    pattern = "\n"
    for line_count in range(1, height + 1):
        pattern += pyramid_line(character, line_count, height)
    return pattern


def main():
    height = int(input("\n\tEnter the number of lines for the pyramid: "))
    brick_character = input("\tEnter the character from which the pyramid should be made: ")
    print(brick_character)
    print(pyramid_string(brick_character, height))


# Start the program
if __name__ == "__main__":
    main()
