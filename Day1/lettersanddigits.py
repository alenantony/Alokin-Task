"""Program to count number of letters, digits and symbols in a string."""

string = input("Enter any string: ")

alphabet_count = 0
digits_count = 0
symbols_count = 0

for i in string:
    if i.isalpha():  # To check if the character is an alphabet.
        alphabet_count += 1
    elif i.isnumeric():  # To check if the character is a number.
        digits_count += 1
    else:  # To count symbols.
        symbols_count += 1

print(f"Number of letters: {alphabet_count}")
print(f"Number of digits: {digits_count}")
print(f"Number of symbols: {symbols_count}")
