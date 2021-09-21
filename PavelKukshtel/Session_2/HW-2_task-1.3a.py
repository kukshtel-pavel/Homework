### Task 1.3
###Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
###Examples:
###```
###Input: ['red', 'white', 'black', 'red', 'green', 'black']
###Output: ['black', 'green', 'red', 'white', 'red']
###```


inputData = ['red', 'white', 'black', 'red', 'green', 'black']
words = [word for word in inputData]
print(",".join(sorted(list(set(words)))))
