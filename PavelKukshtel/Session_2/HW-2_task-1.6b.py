### Task 1.6
###Write a program which makes a pretty print of a part of the multiplication table.
###Examples:
###```
###Input:
###a = 2
###b = 4
###c = 3
###d = 7
###
###Output:
###	3	4	5	6	7	
###2	6	8	10	12	14	
###3	9	12	15	18	21	
###4	12	16	20	24	28
###```

minVert = int(input('Enter minimal vertical multiplier_'))
maxVert = int(input('Enter max vertical multiplier_'))
minHoriz = int(input('Enter minimal horizontal multiplier_'))
maxHoriz = int(input('Enter max horizontal multiplier_'))
if minVert > maxVert or minHoriz > maxHoriz:
    print('Неверный ввод')
else:
    for j in range(maxHoriz - minHoriz + 1):
        print('', minHoriz + j, sep='\t', end='')

    for i in range(maxVert - minVert + 1):
        print('\n', minVert + i, end='\t')
        for y in range(maxHoriz - minHoriz + 1):
            print((minVert + i) * (minHoriz + y), '', sep='\t', end='')
            