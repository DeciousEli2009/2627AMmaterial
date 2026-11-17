print("This is the mario tower printer made by Eli Decous. There is no limit to the amount you can print so be careful! Do enough and it can take some time to generate!")

amount = input("Give me a number: ")
while not amount.isdigit():
    amount = input("Please make sure the number is in integer")
print(f"Okay, {amount} lines!") 

amount = int(amount) #makes the amount an int so i can multiply by it


#this is what makes the actual triangle. Look below for details on how it works


for tiles in range(amount): #this is like a row. Way i thought of it was like a series of bathroom tiles 
    hashtag = "#" * (tiles + 1) #
    space = " " * (amount - 1 - tiles) #
    print(space + hashtag + "  " + hashtag) #prints everything
#Sources:
'''
phttps://www.w3schools.com/python/ref_string_isdigit.asp
used this to figure out the isdigit thing i did with the inital while loop.


'''
