"""Function to get time of execution of a function."""
# import time

# a = input("Ente a value:")

# def multiply_by_2(a):
#     a = a * 2

# result = multiply_by_2(a)

from time import process_time # importing time

def main_function(decorator_function): # function to call decorator
    def sub_function():
        start_time = process_time()
        print("before the function")
        deco =  decorator_function()
        print("after running function")
        end_time = process_time()
        print("Time took for function: ", end_time-start_time)
        return deco
    return sub_function

def sending_function(): # function calling inside the function
    print("on function")
    return "test_sucess"

send_function = main_function(sending_function)

start_time = process_time()
print(send_function()) # calling the assigned main function
end_time = process_time()
print("Time took for function: ", end_time-start_time)