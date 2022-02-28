"""Program to group the odd and even numbers
from user input.
"""

list1 = [int(item) for item in input("Enter the list item : ").split()]

odd_list = []
even_list = []


def filter_number(list1):
    """function to create list of odd numbers and even numbers.
    """

    for number in list1:
        if number % 2 == 0:  # To check if a number is even or not.
            even_list.append(str(number))
        else:
            odd_list.append(str(number))

    # sorting lists in ascending order
    even_list.sort()
    odd_list.sort()

    print(f"Even numbers : {', '.join(even_list)}")
    print(f"Even numbers : {', '.join(odd_list)}")


filter_number(list1)
