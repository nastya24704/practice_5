number = int(input())
first = number//1000
second = number//100 -first*10
third = number//10 - first*100 - second*10
fourth = number - first*1000 - second *100 - third * 10
if first==fourth and second==third:
    print('настоящее')
else:
    print('кривое')
