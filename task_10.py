pin = int(input())
if pin < 1000 or pin>9999:
    print('ERROR')
else:
    first = pin//1000
    second = pin//100 - first*10
    third = pin//10 - first*100 - second*10
    fourth = pin%1000
    if pin<=2050 and pin>=1900:
        print('ERROR')
    else:
        if first == second or first == third or first == fourth:
             print('ERROR')
        elif second == third or second == fourth or third == fourth:
             print('ERROR')
        else:
            print('OK')
