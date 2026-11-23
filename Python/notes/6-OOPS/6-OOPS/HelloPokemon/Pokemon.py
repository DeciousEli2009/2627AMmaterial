'''
    Classes and Objects
    primitive = bool, intergers, floats, character
    non-primitive = string, list, json
        classes and objects => your own data type

        RULES OF THUMBS
            1. Do you need a variable that stores a lot of stuff 
                and does a lot of stuff ?
            2. Do you need some type of abstract concept that is reusable 
            3. Do you need to stop repetitive code?
            4. Your classes should be in a seperate file
            5. your file name, should be the same number as your class*
            6. Capitilization is key to state if you're using a Class or an Object
            7. Comment the crap out of your code....You'll forget or get fried...
'''
#import
#define your class
class Pokemon:  #The file name and the class name are SPELLED THE SAME

    #define globsl variables aka public variables
    #build your constructor - initial code to set up an obj class
    def __init__(self,nickname,species,level,p_type,hp):
        self.nickname = nickname
        self.species = species
        self.level = level
        self.p_type = p_type
        self.hp = hp

    #build your getters and setters aka accessors and mutators
    def getHP(self):
        return self.hp

    def setHP(self,newHP):
        self.hp = newHP

    def evolve(self,newSpecies):
        self.species = newSpecies

    def takeDamage(self,damage):
        self.hp -= damage


    #specific functions/methods
    #toString - by deafault it prints its RAM location
    #   toString or __str__ will replace the deafault print
    def __str__(self):
        out = ""
        out += self.species+"\n"
        out +="\t"+self.nickname
        return f"{self.nickname} the {self.species}" 
