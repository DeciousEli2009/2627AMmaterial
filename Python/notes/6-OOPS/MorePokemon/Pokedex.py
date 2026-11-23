from Pokemon import Pokemon

pokedex = []


#read the data from the file
with open("151Pokemon.txt","r") as file:
    #r is for read only
    lines = file.readlines() #puts the entire file into lines
#save the data to a pokedexList
print(lines)
for eachLine in lines[1:]:
    # string.rstirp.split
    # rstrip -> strip any tailing blank space
    # split -> split the string based off of ","
    parts = eachLine.rstrip().split(",")
   # print(parts[5:]) #list

    pokedex.append(Pokemon(parts[0],parts[3],parts[4],parts[5:]))
#functions

#mainLoop
#print out eachItem in list
print(f"Total Pokemon Imported: {len(pokedex)}")





#For eachPokemon in pokedex:
# print(eachPokemon)
'''
    Ask the user for a pokemon if htey ask for one in the db
        output:
            level species has the following attacks
                attack 1
                attack 2
                attack 3


        no need to loop the program until they say quit just one time is necessary

'''


