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
CandyChoice = input("Do you want any candy? We have a special sale where all Candy is the same price of 2$! (y/n)")
if CandyChoice == "n":
    print(f"Your total is: ${subtotal}")
else:
    Candy = input(''' 
    Which candy would you like? Here are our options
    (M)M&M's
    (S)Skittles
    (WFC)Worlds Finest Chocolate Bar
    (RC)Reece's (Comes with 2)
    (NC)Nerds Cluster (Comes with 3)''')
    if Candy == "m" or "s" or "wfc" or "rc" or "nc":
        subtotal+=3
print (f"Okay, your total is {subtotal:.2f}") 

if CandyChoice == "n":
    Candy = "none"



#iteration 4 butter


butter = input("How many squirts of butters?" )
subtotal += int(butter)*.25
print(f"subtotal: ${subtotal:.2f}")



#iteration 5 - checkout screen

#'''
#Your order:
#    popcorn =
#    drink =
 #   candy =
  #  butter # =
#
 #   discount (When you buy popcorn drink and candy)
  #   
   # subtotal =
    #tax =
    #total = 


#'''
#print(f'''Okay, heres your checkout

 #   popcorn = {popcorn}
  #  drink = {soda}
   # candy = {Candy}
    #squirts of butter = {butter}

    #subtotal = {subtotal}
    #tax = {subtotal * .07} 
    #Total = {subtotal * 1.07}''')
'''
quit trying to make this work :sob:
    Note to eli again 
    NEVER TRY AND MAKE WHATEVER THIS BS IS WORK EVER AGAIN!!!!! THIS IS STUPID!!!!
    one more time to make sure ik QUIT TRYING THIS!!!1
if popcorn == "s" or "m" or "l":
    PD = 1
else:
    PD =10
if soda == "s" or "m" or "l":
    SD = 1
else:
    SD =10
if Candy == "nc" or "s" or "wfc" or "m" or "rc":
    CD = 0
else:
    CD = 10
if PD + SD + CD == 2:
    discount = 1
if PD + SD + CD >i:
    discount = 0
    '''
discount="NA"
if not(popcorn == "n'" or soda == "n" or Candy =="n"):
    print("Here's a dollar off discount")
    subtotal -=1
    discount=True
print("\n"*50) #clears the scree. Look for a better way to do this, Bander said there is one. Consider this hw. Update tmr?

print(f'''
    Okay, here is your total
      
    popcorn = {popcorn}
    drink = {soda}
    candy = {Candy}
    squirts of butter = {butter}

    subtotal = {subtotal:.2f}
    tax = {subtotal * .07:.2f}
    discount = {discount}
    Total = {subtotal * 1.07:.2f}''')

