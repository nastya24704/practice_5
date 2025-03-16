number = int(input())
if number < 11 or number > 14:
    if number % 10 == 1:
        print(number, 'попугай')
    elif number % 10 > 1 and number % 10 < 5:
        print(number, 'попугая')
    else:
        print(number, 'попугаев')
else :
        print(number, 'попугаев')
