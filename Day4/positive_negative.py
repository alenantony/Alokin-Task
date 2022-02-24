array = [0, -1, 2, -3, 5, 7, 8, 9, -10]

# sorted_array = sorted(array, key=lambda item: item)
# print(sorted_array)

# sorted_array = sorted(array, key=lambda item: item , reverse=True)
# print(sorted_array)

# sorted_array = sorted(array, key=lambda item: 0 if item == 0 else 1/item)
# print(sorted_array)

array = [-1, 2, -3, 5, 7, 8, 9, -10]
sorted_array = sorted(array, key=lambda item:-1/item)
print(sorted_array)

array = [0, -1, 2, -3, 5, 7, 8, 9, -10]
sorted_array = sorted(array, key=lambda item: -1 if item == 0 else -1/item)
print(sorted_array)