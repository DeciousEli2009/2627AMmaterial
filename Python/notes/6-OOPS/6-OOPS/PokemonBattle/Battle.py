import random
import Pokemon

def create_pokemon(choice):
    if choice == "Bulbasaur":
        attacks = {
            "Tackle": (20, "Normal"),
            "Vine Whip": (25, "Grass"),
            "Razor Leaf": (35, "Grass")
        }
        return Pokemon.Pokemon("Bulbasaur", "Grass", 110, 8, attacks)

    elif choice == "Squirtle":
        attacks = {
            "Tackle": (20, "Normal"),
            "Water Gun": (25, "Water"),
            "Bubble Beam": (35, "Water")
        }
        return Pokemon.Pokemon("Squirtle", "Water", 105, 10, attacks)

    elif choice == "Charmander":
        attacks = {
            "Scratch": (20, "Normal"),
            "Ember": (25, "Fire"),
            "Flamethrower": (35, "Fire")
        }
        return Pokemon.Pokemon("Charmander", "Fire", 100, 6, attacks)

    elif choice == "Pikachu":
        attacks = {
            "Quick Attack": (20, "Normal"),
            "Thunder Shock": (25, "Electric"),
            "Thunderbolt": (35, "Electric")
        }
        return Pokemon.Pokemon("Pikachu", "Electric", 95, 5, attacks)


# --- Game Setup ---
roster = ["Bulbasaur", "Squirtle", "Charmander", "Pikachu"]
print("Available Pokémon:", ", ".join(roster))

player_choice = input("Choose your Pokémon: ").strip().title()
while player_choice not in roster:
    player_choice = input("Invalid choice. Pick Bulbasaur, Squirtle, Charmander, or Pikachu: ").strip().title()

# CPU picks a random different Pokemon
cpu_roster = [p for p in roster if p != player_choice]
cpu_choice = random.choice(cpu_roster)

player = create_pokemon(player_choice)
cpu = create_pokemon(cpu_choice)

print(f"\nYou chose {player.getName()}!")
print(f"Rival sent out {cpu.getName()}!")
print("-" * 40)

# --- Turn-Based Battle Loop ---
while not player.isFainted() and not cpu.isFainted():
    print("\n" + str(player))
    print(str(cpu))

    # Player's Turn
    move_list = list(player.getAttacks().keys())
    print("\nYour Attacks:")
    for i in range(len(move_list)):
        move_name = move_list[i]
        power, m_type = player.getAttacks()[move_name]
        print(f"  {i + 1}. {move_name} ({m_type} | Power: {power})")

    move_num = int(input("Select attack (1-3): "))
    while move_num not in [1, 2, 3]:
        move_num = int(input("Pick 1, 2, or 3: "))

    chosen_attack = move_list[move_num - 1]
    player.attack(cpu, chosen_attack)

    # Check if CPU fainted before CPU gets a turn
    if cpu.isFainted():
        print(f"\n{cpu.getName()} fainted! You win!")
        break

    # CPU's Turn (picks one of its 3 attacks at random)
    cpu_moves = list(cpu.getAttacks().keys())
    cpu_attack = random.choice(cpu_moves)
    cpu.attack(player, cpu_attack)

    # Check if Player fainted
    if player.isFainted():
        print(f"\n{player.getName()} fainted! You lost!")
        break

