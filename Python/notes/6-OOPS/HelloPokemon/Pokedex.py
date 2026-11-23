#import
from Pokemon import Pokemon

#global variable
#object = Constructor()
bulb = Pokemon("Bulbasaur","bub",4,"Grass",50)
vul = Pokemon("Vulpix","fox", 13, "Fire", 37)
char = Pokemon("Charzard", "dragoon", 24, "Fire", 76)


x = 4
y = "this is an object"     #technically a String

print(bulb)     #technically not a good idea
print(bulb.getHP())     #more professional
print("\n"*5)

print (vul)
print(vul.getHP())
vul.takeDamage(10)
print(vul.getHP())

myPokedex = []
myPokedex.append(Pokemon("Vulpix","fox", 13, "Fire", 37))
myPokedex.append(Pokemon("Ninetails","big fox",13,"fire",37))

for i in range(len(myPokedex)):
    print(f"{i+1} {myPokedex[i]}")
