'''
    List data type
        primitive data types
        non primitive data types
        Sequence data structures - Iterable data
    List = One objetct with multiple pieces of data
        I think of this as a backpack
                            inventory
                            grocery list 


'''
name = "x"
######## Create ########
ChristmasList = []
GroceryList = ["turkey butts", "ham", "egg nog", "Ssweet potato pie", "queso"]
genericlist = [1, "string", ["o", "l", 2] ,name]
print(genericlist)

print(genericlist)
ChristmasList.append("RTX590") #Adds items to the list
ChristmasList.append("64GB DDR5") #Adds items to the bottom
ChristmasList.append("NVIDIA Sparkchip")
######## Read ########
#access an item from the list
print(ChristmasList)
print(ChristmasList[0])

ChristmasList.append("1 ham sandwich")
print(ChristmasList)
print(len(ChristmasList)) # how long is the list
print(ChristmasList[-1]) # last item
print(ChristmasList[2:]) #item 2 the end
# list[ startValue : endValueNotIncluded ]


######## Update ########

ChristmasList[1] = "32 GB DDR5"
print(ChristmasList)
ChristmasList[2: ] = "poop"
print(ChristmasList)

newList = GroceryList + ChristmasList # No -, /, or * =, only addition
print(newList)


######## Delete ########
print("\n"*5)



print(newList)
newList[0] = " " #Deletes but leaves the space
print("\n")

item = newList.pop() #returns my data and deletes it from the last
print(item, newList)


item = newList.pop(3) #returns item 3
print(item,newList)
print()

del newList[1]



newList=[]
print(newList)





#### MORE USEFUL THINGS ####
Chess=["pawn","rook","horse","cross","bishop","not cross"]

i=0
while(i<9):
    Chess.append("pawn")    
    i+=1
print(Chess)

print(Chess.index("not cross"))

Chess.pop(Chess.index("not cross"))
print(Chess)
if "not cross" in Chess: #Check if object is in list
    print("attack")
else:
    print("Long Live The Queen!")


print("pawn" in Chess)

print(f"pawn count {Chess.count("pawn")}") 


while(Chess.count("pawn") > 8):
    Chess.pop(Chess.index("pawn"))

print(f"pawn count {Chess.count("pawn")}")
print(Chess)


Chess.sort()
print(Chess











      )
