# Name: delete_small_words_with_for.py
# 
# Description
# This program uses a 'for' loop when deleting elements in a list of words that
# are less than 4 characters long.
# 
# It does not work because the we are modifying the length of the list after we
# have set the number of iterations for the loop.
# 
# #

# # Start the program
def main():
    words = ["Welcome", "to", "the", "island!"]

    print("\n", words)
    for i in range(len(words)) :
        word = words[i]
        print("\ti: {}, {}".format(i, words[i]))
        if len(word) < 4 :      
            words.pop(i) 

    print("\n", words)

if __name__ == "__main__":
    main()
#At the start of the for loop, Python uses the list length to determine how many times to perform the loop. 
# If you change the size of the list then Python will try to process elements beyond the new list length.