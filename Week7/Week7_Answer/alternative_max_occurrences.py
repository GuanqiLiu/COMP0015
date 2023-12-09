import random

def max_occurrences(lis):
    most_frequent_digit = []
    mode = 0
    if len(lis) > 0:
        frequencies = digit_frequencies(lis)
        mode = max(frequencies.values())
        for k,v in frequencies.items():
            if v == mode:
                most_frequent_digit.append(k)
    return most_frequent_digit, mode

def digit_frequencies(lis):
    frequencies = {}
    for num in range(10):
        frequencies[num] = lis.count(num)
    return frequencies

def generate_list(length):
    out_lis = []
    for i in range(length):
        out_lis.append(random.randint(0, 9))

    return out_lis


def main():
    lis = generate_list(10)
    most_frequent_digits, occurs = max_occurrences(lis)
    print(f"List of digits: {lis}")
    print(f"Number: {most_frequent_digits} appears most frequently - {occurs} times")

    lis = []
    most_frequent_digits, occurs = max_occurrences(lis)
    if most_frequent_digits == 0 and occurs == 0:
        print("The list is empty")
    else:
        print(f"List of digits: {lis}")
        print(f"Number: {most_frequent_digits} appears most frequently - {occurs} times")

if __name__ == "__main__":
    main()    