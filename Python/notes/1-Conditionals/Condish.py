'''

Boolean data type =- True or False also T or F
You can think of this as 1 or 0, as thats how the computer will see it.

Conditionals = Code that does something based on a condition
    Usually the condition is going to be a boolean expressions



    if booleanExpression == True =
        then do this
    elif booleanExpression == True =
        then do this
    else
        then do this


'''

x = True
y = False

print(x,y)

print(10 > 5)

'''
Logic operators
    < > <= >=

    == if it is equal to
    = sets stuff equal to
    is -> Checks if the memory location is the same
        This is more of a later concept but keep it in mind (Mostly just dont use this yet!!!)
    not or ! => opposite of boolean to the right 
    



'''

if x == y:
    print("you may proceed")
#if x and y are not the same thing then, ir does nothing

if x -- (not y):
    print("you may NOT proceed")


y = 2*x+4
x,y = 0,0

print(0 == y)


y < 2* x +4
if(y<0):
    print("shade towards 0")

else:                                               #if all else fails
    print("shade away from 0")

if(y<0):
    print("shade towards 0")
elif (y == 0):
    print("y does = 0")
else:
    print("shade away from 0")




temp = int(input("Whats the temperature of water? "))
if temp <= 32:
    print("solid state")
elif temp >= 212:
    print("GAS")
else: 
    print("Liquid")


'''
 Rules of thumb
 1. FIgure out how many outputs there will be

        Example: If 3 outpurs, then if, elif else
                 If 4 outputs, if, elif, elif, else
                 If 2 outputs, if, else
                    BUT you dont always need an else

                2. If nothing needs to happen if all else fails
                                                    then dont have else

'''



'''
Compound COnditionals or Complex Conditionasl

    and -> boolean == true and boolean == true
        as in both sides of the and are true
            then the result is true
    or -> only one side needs to be true


'''


username = input("un: ")
password = input("pw: ")

if  username == "eli" and password == "123456":
    print(f"Welcome {username}")


#This is the same as the above. Compound/Complex condtions are just simply nested. Usually getting functionality is the end goal over the appeal. Do try and get the complex if possibke

if username == "eli":
    if password == "123456":
        print(f"Welcome {username}")

if username and password == "eli":
    print("Your username and Password cannot match")

if username and password == "elijah":
    print("password and username cannot match")



'''
Weird things about python

If int or str is either 0 or lnak
    it is false
else:
    anything other than 0 or blank is true

'''
