import math
import turtle
coord_xC = float(input())
coord_yC = float(input())
coord_r = float(input())
coord_x = float(input())
coord_y = float(input())
dot_r = math.sqrt(coord_x**2 + coord_y**2)

if coord_r > dot_r:
    print('Точка внутри окружности')
elif coord_r == dot_r:
    print('Точка на окружности')
else:
    print('Точка вне окружности')

turtle.penup()
turtle.goto(coord_xC, coord_yC - coord_r)
turtle.pendown()
turtle.circle(coord_r)
turtle.penup()

turtle.goto(coord_x, coord_y)
turtle.pendown()
turtle.dot(7, 'red')
turtle.penup()

turtle.goto(coord_xC-coord_r, coord_yC- 2*coord_r)
turtle.pendown()
if coord_r > dot_r:
    turtle.write('Точка внутри окружности')
elif coord_r == dot_r:
    turtle.write('Точка на окружности')
else:
    turtle.write('Точка вне окружности')
turtle.done()
