import re

value = '+1(243) 456-3424'
regex = r"^[+][1][(](\d{3})[)] (\d{3})[-](\d{4})$"
if re.fullmatch(regex, value):
    print("yes")

# r = lambda a : a + 15
# print(r(10))
# r = lambda x, y : x * y
# y = r(2, 4)
# print(y)