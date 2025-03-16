import math
coord_xC = float(input())
coord_yC = float(input())
coord_r = float(input())
coord_x = float(input())
coord_y = float(input())
dot_r = math.sqrt(coord_x**2 + coord_y**2)
if coord_r >= dot_r:
    print('Точка внутри окружности')
else:
    print('Точка вне окружности')
