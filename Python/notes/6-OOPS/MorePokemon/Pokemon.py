'''
    Create a Pokemon
    __init__ species, level, hp, moves[]

    getMoves()

    setSpecies()

    __String__

'''
class Pokemon:
    def __init__(self,species, level, hp,moves):
        self.species = species
        self.level = level
        self. hp = hp
        self.moves = moves


        def getMoves(self):
            return self. moves

        #evolve a pokemon
        def setSpecies(self,newSpecies):
            self.species = newSpecies
        def __string__(self):
        #Converts list to string
            movesFormatted = ", ".join(self.moves)
            out=self.species+"\n"
            out+=f"\t{self.level}\n"
            out+=f"\t{self.hp}\n"
            out+=f"\t{self.movesFormatted}\n"
            return out
            

