ui = input("Hey, Guess what? ")  #iterator
while(ui!="wsp" and ui !="yo" and ui!="y"): #while statement

    ui = input("Hey, guess what? ") #do algorithm
print("Turkey Butt") # iterate
print() #rest of code





'''
Ask user for a number between 1-10

If the user the is wrong allow them to guess again and tell tehm higher or lower. 
And if they get it tell tehm congrats!
'''

secret = 7
ui = input("Guess a number 1-10")
while(int(ui)<secret):
    ui = input("Guess higher")

while(int(ui)>secret):
    ui = input("Guess lower")

if ui==secret:
    print("Yay Congrats!")










