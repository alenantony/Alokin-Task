array = [-1, 2, -3, 5, 7, 8, 9 ,-10]

sorted_array = [numbers for numbers in array if numbers < 0] + [numbers for numbers in array if numbers > 0]

print(array)

