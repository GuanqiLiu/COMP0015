'''
File: mars_weight.py

Description: prompts the user for their weight on earth and calculates their weight on mars.
An earthling's weight on mars is 37.8% of their weight on earth.
'''

def main():
    # 1.  Get the user's weight on earth.
    users_earth_weight_str = input ("Please enter your weight on earth: ")
    #convert the user's weight from a string to a float.
    users_earth_weight = float (users_earth_weight_str)

    # 2. Convert the weight to mars weight.
    mars_weight = users_earth_weight * 0.378

    # 3. Print the calculated mars weight. str把他变成string
    #print ("Your mars weight is : " + str(mars_weight))
    print (f"Your mars weight is : {mars_weight:.2f} ")

if __name__ == '__main__':
    main()