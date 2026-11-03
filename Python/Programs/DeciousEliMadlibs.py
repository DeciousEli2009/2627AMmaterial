print("Hello this is a madlibs python program made by Eli Decious. I tried adding some fun easter eggs in this, so try and collect all of them for a secret bonus ending to the madlibs!!!!!")

username = input(''' To start the madlibs, you must answer some quetions. The ending will be filled in with your answers!!!
           The first question is simple. What is your name?: ''')

ice = input(f'''Hey {username}, Its nice to meet you! Now, the second question

What is your favorite flavor of ice cream????: ''')

cod = input(f''' Awesome {username}! {ice} flavor is totally delicious! One of the best!!!

Now, do you prefer cats or dogs???(: ''')
print()
if cod == "dogs":
    print("Lame!! Cats are WAY better! I'll still let you proceed tho....Even tho you are wrong")

elif cod == "cats":
    print("Ha! Cats are SO much better!!!")

print()
living = input(f"Now, what do you live in? A house, Apartment, or a mansion? ")
print()
if living == "mansion":
    print("Liar!!! Dont lie in your madlibs dude!!!")
print()
rest = input(f"So i know you live in a {living}, but what do you sleep on? A bed, couch, or chair? ")
print()

move = input(" What do you use to travel? A bus, car or do you just walk? (B, W, C) ")
print()
if move == "B":
    move = "Took a bus"
elif move == "W":
    move = "walked"
elif move == "C":
    move = "Drove"

fuser = input(" What is your best friends name???")
print()
if fuser == "Eli Decious":
    print("Aww, Thank You!!")
print()
rst = input(f"What resturaunt do you and {fuser} like to go to together?")
print()
meal = input(f"What do you wanna get to eat at {rst}")
print()
drink = input(f"Great choice, {meal}s are delicious!! What drink would you want with that?")
print()
size = input(f"Alright, {meal} with {drink}! What size would you like for that? Kids(k), Regular(R), or the Mega sized meal ")
print()
clean = input(f"What do you do to clean yourself? Shower(S) or Bath(B)?")
if clean =="B":
    clean = "Bath"
elif clean == "S":
    clean = "Shower"

print(f'''Now...Time for the madlibs story!!


      
      My name is {username}, and I {move} to the store to pickup my favorite ice cream flavor {ice}! I then {move} back to my {living}, where I sat on my {rest} to eat all of my {ice} flavored ice cream. I ate the entire thing and it made me SO tired I needed to take a quick power nap. When I woke up I looked outside my windoq and saw 2 {cod} outside! I love {cod}!!! This day is really starting to turn out well! I looked at the time and it was 3:15,I told my best friend {fuser} that we would hangout at {rst} our favorite resturant to go to together. So I {move} to {fuser}'s house and we went to {rst}. When we arive at {rst} I looked at the menu and couldn't decide what what to eat! I ended up choosing {meal}. I also got a {drink} to drink. The size of my meal and drink was {size}. After me and {fuser} eat at {rst}, I {move} back to my {living}. I notice that the {cod} are both still there! They are sleeping just outside my {living}!! I decide to adopt them and bring them inside. All this work today made me quite tired. So I go over to my {rest} to take a power nap. When I wake up its 11:22! I way overslept!! I quickly take a {clean} and get back in my {rest} to go back to sleep. This really was a good day!!!''')






'''





'''



