subjects_1 = int(input())
subjects_2= int(input())
subjects_3 = int(input())
if subjects_1 == subjects_2 and subjects_3==subjects_1:
    print(3)
elif subjects_1 != subjects_2 and subjects_3!=subjects_1 and subjects_3!=subjects_2:
    print(1)
else:
    print(2)
