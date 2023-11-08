def perfect(x):
    sum = 0
    for number in range (1,x+1):
            
        if x % number == 0 and number != x :
            sum += number 
    #return sum 
            
    if sum == x:
        return True
    else:
        return False


def all_perfect(y):

        for number in range (1,y):
            if perfect (number) == True: 
                print (number)

def main():

    input_number = int (input("Enter a number :"))
    all_perfect(input_number)
   

if __name__ == "__main__":
    main ()

    