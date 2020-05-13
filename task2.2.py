import math


def angles():
    angle_ab = math.degrees(math.acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b)))
    angle_bc = math.degrees(math.acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c)))
    angle_ac = math.degrees(math.acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c)))
    return print(f'Angle A = {angle_ab}\nAngle B = {angle_bc}\nAngle C = {angle_ac}')


print('Input the values of the sides of the triangles: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + c > b and a + b > c and b + c > a:
    angles()
else:
    print("Triangle doesn't exist!")
