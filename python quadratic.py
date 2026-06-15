```python
# quadratic.py
import math
a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))
d = b*b - 4*a*c
if (d > 0):
    print("roots are real and equal")
elif (d == 0):
    print("roots are real and equal")
else:
    print("roots are complex")
root1 = (-b + math.sqrt(abs(d))) / (2*a)
root2 = (-b - math.sqrt(abs(d))) / (2*a)
print("root1=", root1)
print("root2=", root2)
