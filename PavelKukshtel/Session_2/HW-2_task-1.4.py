### Task 1.4
##Write a Python program to sort a dictionary by key.


def dictionairy():

    key_value = {}

    # Initializing value by  taxi phone number (Minsk)
    key_value[5] = 152
    key_value[6] = 7788
    key_value[3] = 135
    key_value[4] = 284
    key_value[1] = 7565
    key_value[2] = 7785

    print("Sorted KEYS are:")

    for i in sorted(key_value.keys()):
        print(i, end=" ")


def main():
    # function calling
    dictionairy()


if __name__ == "__main__":
    main()