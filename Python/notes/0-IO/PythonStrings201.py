''' 
    Ask the user for their email
    Print out their username in the format of
    Welcome {username}

'''


email = input("email: ")
username =  email[0:email.find('@')] #When using the the FIND if it cannot find something command it returns -1
#returns -1 because it tells the programmers (me) the error. This is a result in alot of languages.
print(f"Welcome, {username}!")

first = username[0:username.index(".")] #When using the index command, if it fails it will break the program. 
last = username[username.index("."):]



print(first.title(),last.title())





#This does not work. this is because of the capital ZI
name = "zoe"
#name[0] = "Z" this is a no no
name = name.replace("z" , "Z") #returns the replaced version. Make sure to include the original variable in the replace.
print(name)



'''
Other common methods

strip, lstrip, rstrip == strip removes all spaces l and r versions are left and right versions
startswitch and endwith == searching tools
split == splits based on a char


'''



















''' 
Challenges From Bander
C1: input a credit card number and have it output the following format: **********####
C2: Have the user type in a website: https://defense.cyber.gov and check if it is using a secure protocol also check if its a .gov website

'''


file = input(


















