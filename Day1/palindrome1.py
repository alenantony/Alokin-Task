"""Program to check if a string is a palindrome or not."""

string = input("Enter a string : ")


def palindrome(string):
    """Function to check if a given input is a palindrome or not."""

    if string == string[::-1]:
        print("Entered string is a palindrome")
    else:
        print("Entered string is not a palindrome")


palindrome(string)
