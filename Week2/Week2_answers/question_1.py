"""
1. Write a console program that displays all the numbers in the Fibonacci Sequence up to a given max, starting with 0. The Italian mathematician Leonardo Fibonacci devised the Fibonacci sequence as a way to model the growth of a population of rabbits. The first two terms in the sequence are 0 and 1, and every subsequent term is a sum of the previous two terms. (The Fibonacci sequence has numerous applications in computer science and shows up in surprising places. It's used to compute logarithms, index and retrieve data, and as a building block in some route-planning algorithms.)

Output from one example run:

This program lists the Fibonacci sequence.
Max value? 10000
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
"""


def main():
    print("This program lists the Fibonacci sequence.")
    max_value = int(input("Max value? "))

    a = 0
    b = 1
    while a <= max_value:
        print(a, end=", ")
        temp = a
        a = b
        b = temp + b

if __name__ == "__main__":
    main()






