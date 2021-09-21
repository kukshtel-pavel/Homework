### Task 1.6
###Write a Python program to convert a given tuple of positive integers into an integer. 
###Examples:
###```
###Input: (1, 2, 3, 4)
###Output: 1234


def tuple_converter(numbers):
    result = int(''.join(map(str, numbers)))
    return result


numbers = (1, 2, 3, 4)
print("Original numbers - INPUT ")
print(numbers)
print("Converted to integer - OUTPUT")
print(tuple_converter(numbers))