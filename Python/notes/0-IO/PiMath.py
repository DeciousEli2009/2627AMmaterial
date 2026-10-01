#Notes on math via python. More commented notes as this continues.

#Always remember to use the import features at th TOP of a program
import cmath 
import math

problem1 = ((8/2)+4*16)/3*8

problem2 = (3/81)/(3/7)*8*(2+1*12)

problem3 = (4-2)**2+(16-2)**2

#problem4 = ((7-1/2)**2+(16-2)**2

problem4a = math.sqrt((7-1/2)**2+(1/3-4)**2)                                   

print(f"1. {problem1}")
print(f"2. {problem2}")
print(f"3. {problem3}")
#print(f"4. {problem4}")
print(f"4a. {problem4a}")


print(8^2) #This is a bitwise calculation... idk







#Return a whole number when I divide

print(7/3)
print(math.floor(7/3))
print(7//3)
print(8//3)         #integer divide - returns an integer
#truncates the decimal as in cuts the decimal off
print(59//5)


#find the remainder?... modulus


print(7%3)
print(8%2)



a=2
b=4
c=-7


xp=(-b+math.sqrt(b**2-4*a*c))/(2*a)
xm=(-b-math.sqrt(b**2-4*a*c))/(2*a)
print(f"The roots are: {xp:.2f} and {xm:.2f}")

#imaginery numbers
print(cmath.sqrt(-4))
print(cmath.sqrt(9j))
print(1j*2j)
print(complex(2,3))

subtotal =eval(input("what is the subtotal: "))
#eval makes python figure it out
#int(convets to an int)
#float() converts to a float
#str() String
#bool() true or false boolean
tax = * 0.7
total = subtotal +tax
print(subtotal,tax,total)

subtotal*=1.07


'''math Operator
    +,-,*,/
    += -= *= /=
    =


    not,!,!=,==,<,>,<=,>=           these are logic operators




'''





