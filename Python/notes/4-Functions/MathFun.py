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
def mxplusb(slope, x, yint):
    return slope*x*yint
print(f'''
x | y
-----
0 | {mxplusb(2,0,4)} 
1 |
2 |

'''
for x in range(1,11):
      print(f"{x} | {mxplusb(2,x,4)}")
# quadratic formula (be sure to show the +/-)
def quad(a,b,c):
    xp=-b+math.sqrt(b**2-4*a*c)/(2*a)
    xp=-b-math.sqrt(b**2-4*a*c)/(2*a)
    
    return (xp, xn) #tuple

x1,x2 = quad(1,0,2)
print(x1,x2)



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









