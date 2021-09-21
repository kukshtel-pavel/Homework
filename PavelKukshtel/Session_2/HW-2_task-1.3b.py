### Task 1.3
###Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
###Examples:
###```
###Input: 60
###Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}


i = 1
number = int(input('Please enter a number: '))
while i < number:
    i += 1
    if number % i == 0:
        print(i)