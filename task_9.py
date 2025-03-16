tower_list = input()
tower_1, tower_2, tower_3 = map(int, tower_list.split())
max_t = max(tower_1, tower_2, tower_3)
min_t = min(tower_1, tower_2, tower_3)
if tower_1 != max_t and tower_1 != min_t:
    print(max_t, tower_1, min_t)
elif tower_2 != max_t and tower_2 != min_t:
    print(max_t, tower_2, min_t)
else:
    print(max_t, tower_3, min_t)
