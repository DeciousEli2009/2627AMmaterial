#iteration 1 -popcorn
'''
    Ask what size of popcorn?
        small = $5.00
        medium = $6.00
        large = $7.00
    print out their total
        SUBTOTAL: $_.__
'''

subtotal=0
popcorn = input('''

What size of popcorn?
(s) small = $5.00
(m) medium = $6.00
(l) large = $7.00
(n) no popcorn





''').lower() #forcing the input to be lower
if popcorn == "s" or popcorn == "S":
    subtotal+=5
elif popcorn == "m":
    subtotal=+6
elif popcorn == "l":
    subtotal+=7

else:
    print("No popcorn, But why not??")
print(f"subtotal: ${subtotal}")


    






#interation 2 - soda pop
'''
Ask the user if they want a soda or not
    if they do, what size do they want
        small = 3
        medium = 4
        large = 5
            if they do want a large ask if they want a child size for 38 cents more

print subtotal
'''
soda = input("Do you want a soda? (y/n)").lower()
if soda == "y":
    soda = input(''' 
    Which Size would you like?

    (s)Small
    (m)Medium
    (l)Large
''')
    if soda=="s":
        subtotal+=3
    elif soda=="m":
        subtotal+=4
    elif soda =="l":
        subtotal+=5
        if input("Would you like a childsize for 0.38$ more??? (y/n)?")=="y":
            subtotal+=.38
print(f"subtotal: ${subtotal:.2f}") #:.2f means 2 floating points


#iteration 3 - candy
'''
Do you want any candy?
What type
    m&m's
        plain
        peanut
        pb
        mini
    skittles
        regular
        tropical
    worlds's finest chocolate bars
        wafer
        milk chocolate
        dark chocolate
        almonds
        caramel
    reece's - 2
    nerds gummy cluster - 3
print out the subtotal
    
'''        








#iteration 4 butter



