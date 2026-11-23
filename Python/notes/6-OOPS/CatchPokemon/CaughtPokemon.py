from datetime import datetime       #import datetime

class CaughtPokemon:

    #Xavier notes - static variables
    dex_id = 1  #global varibale for the class

    def __init__(self,trainer,pokeName):
        self.pokemon_name = pokeName
        self.trainer_name = trainer
        self.id = CaughtPokemon.dex_id
        CaughtPokemon.dex_id += 1 # updates the global var
        self.timestamp = datetime.now()     #grabs the current time

    def get_dex_entry_id(self):
        return self.id

    def __str__(self):
        out =f"{self.trainer_name}\t Caught {self.pokemon_name}"
        out+=f"\n\tCaught at {self.timestamp}"
        return out

    
