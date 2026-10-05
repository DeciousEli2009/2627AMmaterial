# Notes on strings in Python. From October 5th 2026


'''
    Primitive: integers, floats, boolean, bit, char

    Non-primitive:
    String, List 

String Data Type
    - Non primitive data type
    - Made up of other datatypes
    - sequence data types => iterable (You can access each element)
                             Technically, called a char array pr a list of chars

    
'''
#IN PYTHON, ALL DATA IS A STRING BY DEFAULT!!!!!!
num1 = input("number: ")
num2 = input("number: ")
print(int(num1) + float(num2))
'''
int => converts something to an int
float => converts something to a float
eval => let Python figure it out




'''





      
# ' " ''' """ == theyre all strings!*



print('bob')
print("bob")
print('''bob''')

#You can do ANY of these but do NEVER use different "''scenarios






print('''"It's a trap quoted by Admiral Ackbar"''')

print("\"It's a trap\" quoted by Admiral Ackbar")

'''
      escape characters

        \n == new line
        \" == "
        \t == tab
        \s == space (but not really used today, mostly for older programs
        \b == backspace
        \d == delete
        \\ == \

    These are older code functions, they are not as used today with the exlcusion of \n that still sees some usage




'''





first = "Brett"
last = "Crawdaddy"

print(first + last)     #concatenates
print(first *2)

fullname=" "
fullname+=first
fullname+=last
print(fullname)
print(fullname)


fullname*=2
print(fullname)


print(len(fullname))




print(first[0])
print(first[3])
#print(first[5])

username = f"{first}.{last}"
email = username+"@stu.evsck12.com"

print(username)
print(len(username))
print(email)
print(len(email))


#string[start;stopNotInclude:step
# ett.C
print(email[2:7])

# dad
print(email[8:13])

#.com
print(email[27:31])
print(email[len(email)-4:])
print(email[-4:])


#print backwards

print(email[::-1]) #prints backwards
print(email[::2]) #prints every other 
print(email[2::4]) #print from 2 to end by 4

import string #IMPORTS ALWAYS AT THE TOP!!! THIS IS BAD PRACTICE
print(string.ascii_letters)
print(string.ascii_lowercase[::-1])
