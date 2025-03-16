hight=float(input())
weight=float(input())
# ИМТ (кг/(м**2))
bmi=round(weight/((hight/100)**2), 2)
if bmi<16:
    print(bmi, 'выраженный дефицит массы тела')
elif bmi >= 16 and bmi<= 18.49:
    print(bmi, 'недостаточная масса тела')
elif bmi>=18.5 and bmi<= 24.99:
    print(bmi, 'норма')
elif bmi>=25 and bmi<= 29.99:
    print(bmi, 'избыточная масса тела')
elif bmi>=30 and bmi<= 34.99:
    print(bmi, 'ожирение первой степени')
elif bmi>=35 and bmi<= 39.99:
    print(bmi, 'ожирение второй степени')
else:
    print(bmi, 'ожирение третьей степени')
