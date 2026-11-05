import math

# distance formula

# pythagorean theroem
'''
def pythag(a**2+b**2=c**2):
 a=input("What is the first number? ")
 b=input("What is the second number? ")
 c=input(" What is the hypotenuse? ")
print(pythag)
'''
# y=mx+b

# quadratic formula (be sure to show the +/-)

# area of a rectangle
def areaOfRectangle(w,h):
    print(w*h)


#volume of a box

def f(x):
    return x**2+4*x+2 #return - the function gives back data

a =areaOfRectangle(6,8)
print(a)
print(f"this much total of sqft {18*a}")

x0=0
x1=2
n=10000
width = (x1-x0)/n

area=0
for i in range(n):
    x = x0+(i*width)
    height = f(x)
    areaa += areaOfRectangle(widith,height)

print(area)









