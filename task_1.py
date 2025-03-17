year = input()
if year%100==0:
  if year%400==0:
    print(366)
  else:
    print(365)
else:
  if year%4==0:
    print(366)
  else:
    print(365)
