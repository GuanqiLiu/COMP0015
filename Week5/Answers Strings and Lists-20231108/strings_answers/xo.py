"""

COMP0015
Prints a pattern of x and o to form a cross

"""

def xo(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == (n - i) - 1:
                print('x', end = '')
            else:
                print('o', end = '')
        print()
    print()




def main():
    xo(5)
    xo(6)





if __name__ == "__main__":
    main()
