def func_compute(n):
    return lambda x : x * n


result = func_compute(2)
print(result(15))

result = func_compute(3)
print(result(15))