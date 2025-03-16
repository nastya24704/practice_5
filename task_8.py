knut = float(input())
galleon= knut//(29*17)
sicl= (knut - galleon*17*29)//29
min_knut = knut - galleon*17*29 -sicl *29
if galleon != 0:
    print(int(galleon), 'галлеонов')
    if sicl != 0:
        print(int(sicl), 'сиклей')
        if min_knut != 0:
            print(int(min_knut), 'кнатов')
        else:
            pass
    else:
        if min_knut != 0:
            print(int(min_knut), 'кнатов')
        else:
            pass
else:
    if sicl != 0:
        print(int(sicl), 'сиклей')
        if min_knut != 0:
            print(int(min_knut), 'кнатов')
        else:
            pass
    else:
        if min_knut != 0:
            print(int(min_knut), 'кнатов')
        else:
            pass
