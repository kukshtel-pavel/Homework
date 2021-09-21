### Task 1.2
###Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
###Examples:
###```
###Input: 'Oh, it is python' 
###Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}


yourStr = input("Enter your string! ")

def charFrequency(yourStr):
    dict = {}
    for n in yourStr:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(charFrequency(yourStr))

