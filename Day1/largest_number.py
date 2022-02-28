"""Program to find the largest number with highest occurence from a list"""

from collections import Counter

user_input = [int(item) for item in input("Enter the list items: ").split()]


def highest_occurance(user_input):
    """Function to find the largest number with highest occurence
    from the list.
    """

    user_input = dict(Counter(user_input))
    sorted_dict = {k: v for k, v in sorted(
        user_input.items(), key=lambda item: item[1],
        )}
    print(sorted_dict)

    sorted_dict = {k: v for k, v in sorted(
        user_input.items(), key=lambda item: item[1], reverse=True
        )}
    print(sorted_dict)


highest_occurance(user_input)
