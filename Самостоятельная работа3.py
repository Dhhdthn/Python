import math

y = int and float(input())
x = int and float(input())
z = int and float(input())
e = int and float(input())
a = math.sin(z)
c = math.cos(y)
v = abs(x)
if (x + y) <= 0:
    print('Error')
elif(e ** abs(x -y) + (x/2)) == 0:
    print('На 0 делить нельзя')
b = y ** pow(v, 1/3) + (c ** 3) * (((abs(x - y)) * (1 + ((c ** 2)/math.sqrt(x + y))))/(e ** abs(x -y) + (x/2)))
print(b)