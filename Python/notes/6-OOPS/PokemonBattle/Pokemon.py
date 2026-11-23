import random

class Pokemon:
    # Constructor: sets up all attributes for a Pokemon object
    def __init__(self, name, p_type, hp, defense, attacks):
        self.name = name
        self.type = p_type
        self.hp = hp
        self.max_hp = hp
        self.defense = defense
        # attacks is a dictionary of { "Attack Name": (damage, attack_type) }
        self.attacks = attacks

    # --- Getters (Accessors) ---
    def getName(self):
        return self.name

    def getHP(self):
        return self.hp
    pass

    def getAttacks(self):
        return self.attacks
    pass

    def isFainted(self):
        if self.hp == 0:
            return True
        pass

    # --- Battle Methods ---
    def checkEffectiveness(self, attack_type):
        # Returns 2.0 for super effective, 0.5 for not very effective, 1.0 for normal
        if attack_type == "Fire" and self.type == "Grass":
            return 2.0
        elif attack_type == "Fire" and self.type == "Fire":
            return 0.5
        elif attack_type == "Fire" and self.type == "Water":
            return 0.5
        elif attack_type == "Water" and self.type == "Fire":
            return 2.0
        elif attack_type == "Water" and self.type == "Water":
            return 0.5
        elif attack_type == "Water" and self.type == "Grass":
           return 0.5
        elif attack_type == "Electric" and self.type == "Water":
           return 2.0
        elif attack_type == "Electric" and self.type == "Electric":
           return 0.5
        elif attack_type == "Electric" and self.type == "Grass":
           return 0.5
        elif attack_type == "Grass" and self.type == "Grass":
           return 0.5
        elif attack_type == "Grass" and self.type == "Fire":
           return 0.5

        # TODO 4: Add all remaining elif branches for super effective (2.0) and
        # not very effective (0.5) matchups between Fire, Water, Grass, and Electric.
        # You will need to research the official Pokemon type effectiveness chart!
        
        else:
            return 1.0

    def attack(self, target, attack_name):
        # Grab base power and element type from the attacks dictionary
        base_damage, attack_type = self.attacks[attack_name]
        print(f"\n{self.name} used {attack_name}!")
        if random.randint(1,100) <= 15:
            print(f"...but {self.name}'s attack missed.")
        # TODO 5: Add a 15% chance for the attack to miss!
        # Hint: Generate a random integer from 1 to 100. If it is <= 15,
        # print "...but <name>'s attack missed!" and use 'return' to exit the method early.
        

        # Check type effectiveness against the target Pokemon
        multiplier = target.checkEffectiveness(attack_type)
        if multiplier == 2.0:
            print("It's super effective!")
        elif multiplier == 0.5:
            print("It's not very effective...")

        # Calculate final damage (subtract defender's defense, minimum 1 damage)
        raw_damage = int(base_damage * multiplier)
        final_damage = max(1, raw_damage - target.defense)

        
        # TODO 6: Call target's takeDamage method and pass in final_damage
        
        target.takeDamage(final_damage)

    def takeDamage(self, amount):
        # TODO 7: Subtract amount from self.hp.
        # If self.hp drops below 0, set self.hp to 0 so HP is never negative.
        # Then print: "<name> took <amount> damage! (HP: <hp>/<max_hp>)"
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {amount} damage! (HP:{self.hp}/{self.max_hp})")
        pass

    # toString: displays current stats cleanly
    def __str__(self):
        return f"{self.name} [{self.type}] - HP: {self.hp}/{self.max_hp} | DEF: {self.defense}"

