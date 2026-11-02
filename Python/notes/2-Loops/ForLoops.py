



'''
    for var in list:
    for eachItem in list:
    for i in list:
    for i in range:








'''
#print 0-9
for eachItem in [0,1,2,3,4,5,6,7,8,9]:
    print(eachItem)

#The reange command creates a list.
#Range(startValue, endValueNotIncluded, step)
for eachItem in range(0,10): #0 is where you want to stop 10 is where you want to stop. Do not make this your final number, if 10 is last 9 will print
    print(eachItem,end=",")


for i in range(-10,11):
    print(i,end=",")

    #0-20 even
    #0-20 odds
    #0-100 by 20
    #10 to 0
    #A-Z



print("\n"*4)


for i in range(0,21,2):
    print(i,end=",")
    
for i in range(1,20,2):
    print(i,end=",")

for i in range(0,101,20):
    print(i,end=",")

for i in range(10, -1,-1):
    print(i,end=",")

for i in range(65,91):
    print(chr(i),end=",")

#This is an example of close to how java uses for loops. This is an example of how python does some things better than other languages.

#for(int i=65; i,91; i++){
# print(chr
#}

alpha=["A","B","C"]
alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print()
for eachLetter in alpha:
    print(eachLetter,end=",")

#You can call variables whatever you want and reassign them. This the example of the versatility of Python
classroom=["Brett","Joseph","Mike","Brayden"]
for eachStud in classroom:
    print(eachStud)

helmet,chest,knees,shoes = "Ball cap", "shirt", "levis", "jordans"

armor = [helmet, chest, knees, shoes]
for item in armor:
    print(item)

chest ="Elytra"
armor[1]="jacket"
for item in armor:
    print(item)
#'''



































































