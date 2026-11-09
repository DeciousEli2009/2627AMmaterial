#imports

#globalVar
masterOrderList=[]
entireOrderTotal=0



#functions
def userInput(q,a):
    answer = input(q)
    while(not(answer in a)):
        answer = input(q)
    return answer

def Checkout(order):
    #Show their order
    #Show their tax
    #Show their total
    return

def checkForDiscount(order):
    #are you a vet
    #are you a senior
    return

#mainloop


#loop the entire process until the user is done ordering? aka multiple orders?
orderagain="y"
while(orderagain=="y"):
    #iteration 1 - popcorn
    subtotal=0
    order=[]                            #order will store the user's order
    ui = input('''
    What size popcorn do you want?
        (s) small = $5.00
        (m) medium = $6.00
        (l) large = $7.00
        (n) no popcorn
    ''').lower()   #forcing the input to be lower
    if ui == "s":
        subtotal+=5
    elif ui == "m":
        subtotal+=6
    elif ui == "l":
        subtotal+=7
    else:
        print("No Popcorn, but why?")
    order.append(ui)               #appending or adding to the order their popcorn order
    print(f"subtotal: ${subtotal}")

    #iteration 2 - soda pop
    userInput = input("Would you like a drink? (y/n)").lower()
    if userInput=="y":
        userInput = input('''
    What size soda do you want?
        (s) small = $3.00
        (m) medium = $4.00
        (l) large = $5.00
    ''')
        if userInput=="s":
            subtotal+=3
        elif userInput=="m":
            subtotal+=4
        elif userInput =="l":
            subtotal+=5
            if input("Would you like a child size for .38 more? (y/n)?")=="y":
                subtotal+=.38
                userInput = "c"
    order.append(userInput)               #appending or adding to the order their popcorn order
    print(f"subtotal: ${subtotal:.2f}")    #:.2f means 2 floating points

    #iteration 3 - candy
    flavors=""
    candy = input("Do you want any candy? (y/n)")
    if candy == "y":
        candy = input('''
    What type of candy would you like?
        (m) M&M's - 2.50
        (s) Skittles - 2.50
        (w) World's Finest Chocolate Bars - 2
        (r) Reece's - 2
        (n) Nerds gummi clusters - 3
    ''')

        if candy == "m" or candy == "s":
            subtotal +=2.5
            if candy == "m":
                flavors = '''
        (pl) plain 
        (pe) peanut 
        (pb) peanut butter
        (mi) mini
                '''
            else:
                flavors='''
        (r) regular
        (t) tropical
                '''
                
        elif candy in "wr":
            subtotal +=2
            if candy == "w":
                flavors = '''
        (wa) wafer
        (mc) milk chocolate
        (dc) dark chocolate
        (al) almonds
        (ca) caramel
            '''
        elif candy == "n":
            subtotal+=3

        if flavors != "":
            candy=input(f"Which flavor? {flavors}")
    order.append(candy)
    print(f"subtotal: ${subtotal:.2f}")    #:.2f means 2 floating points  


    #iteration 4 - butter
    butter = input("How many butters " )   #input is ALWAYS a string
    subtotal += int(butter)*.25           #convert the string to an int
    order.append(butter)
    print(f"subtotal: ${subtotal:.2f}")    #:.2f means 2 floating points  

    print(order)    #this is for testing, need to delete out later....  
    #iteration 5 - checkout screen
    discount="NA"
    if not("n" in order):
        print("Here's a dollar off discount ;")
        subtotal -= 1
        discount=True
    print("\n"*50)    #clears the screen, but a better method is out there
    print(f'''
        
        Your Order:
            popcorn  = {order[0]}
            drink    = {order[1]}
            candy    = {order[2]}
            butter # = {order[3]}
        
            discount = {discount}

            subtotal = {subtotal:.2f}
            tax      = {(subtotal * .07):.2f}
            total    = {(subtotal * 1.07):.2f}
    ''')
    orderagain=input("Need another order? (y/n)")
