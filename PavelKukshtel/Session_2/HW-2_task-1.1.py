### Task 1.1
###Write a Python program to calculate the length of a string without using the `len` function.


yourStr = input("Enter your string! ")

# counter variable to count the character in a string
stringCounter = 0
for s in yourStr:
    stringCounter = stringCounter + 1
print("Length of the input string is:", stringCounter)