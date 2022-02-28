"""Program to find largest number with highest occurance from a list."""

list1 = [int(item) for item in input("Enter the list items : ").split()]


def highest_occurance(list1):
    """Function to find the largest number with highest occurance
    from the list.
    """

    highest_occurance = 0
    largest_number = list1[0]

    for number in list1:
        occurance = list1.count(number)
        if occurance > highest_occurance:
            highest_occurance = occurance
            if number > largest_number:
                largest_number = number
        elif occurance == highest_occurance:
            if number > largest_number:
                largest_number = number

    print(f"Largest number is {largest_number} with \
{highest_occurance} occurances")


highest_occurance(list1)
