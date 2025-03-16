entered_list=input()
n, k, m =map(int, entered_list.split())
number_1 = abs(m-k) - 1
number_2 = abs(n-k + m) -1
print(min(number_1, number_2))
