"""Program to check if a string is a palindrome."""

string = input("Enter a string: ")

if string == string[::-1]:
    print("The given string is a palindrome")
else:
    print("not a palindrome")
