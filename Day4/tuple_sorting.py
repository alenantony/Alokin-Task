list_of_tuple1 = [('V', 62 ),('VI', 72), ('VII', 72), ('VIII',70), ('IX',74), ('X',65)]
list_of_tuple = [('V', {'a':62} ),('VI', {'d':72}), ('VII', {'f':72}), ('VIII',{'x':70}), ('IX',{'j':74}), ('X',{'i':65})]

# maximum_minimum = ((max(list_of_tuple1, key=lambda item: item[1].items()))[1], 
#                     (min(list_of_tuple, key=lambda item: item[1].items()))[1])
# print(maximum_minimum)

# print((max(list_of_tuple, key=lambda item: item[1].keys()))[1])


# list_of_tuple = [('V', {'a':62} ),('VI', {'d':72}), ('VII', {'f':72}), ('VIII',{'x':70}), ('IX',{'j':74}), ('X',{'i':65})]

# maximum_minimum = ((max(list_of_tuple, key=lambda item: item[1].keys()))[1], 
#                     (min(list_of_tuple, key=lambda item: item[1].keys()))[1])
# print(maximum_minimum)
maximum_minimum = (
    max(list_of_tuple1, key=lambda item: item[1])[1],
    min(list_of_tuple1, key=lambda item: item[1])[1]
)

print(maximum_minimum)

value = (
    list(max(list_of_tuple, key = lambda item: [i for i in item[1].values()])[1].values())[0],
    list(min(list_of_tuple, key=lambda item: [i for i in item[1].values()])[1].values())[0]
)
print(value)