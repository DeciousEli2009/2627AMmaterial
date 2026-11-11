#import

#global variable
masterOrderList=[]
entireOrderTotal=0

#functions
#replace all input() with new version to check for correct answers
def userInput(q,a):
    answer = input(q)
    while(not(answer in a)):
        answer = input(q)
    return answer

def orderItem3Option(item,sizes,prices ):
    #Asks teh user if they want the item y/n
    ui = userInput(f"Would you like a {item} (y/n)",["y","n"])
    if ui == "y":
        ui = userInput(f"What size {item} do you want? {sizes}",sizes)
        indexOfChoice = sizes.index(ui)
        return sizes[indexOfChoice],prices[indexOfChoice]
        
    #If they do, tehn what size s/m/l
    
    #Return the order choice and price
    return "n",0

orderItem3Option("popcorn",["s","m","l"],[1,2,3])



def checkout(order):
    #show the order
    #show tax
    #show total
    return 

def checkForDiscount(order):
    #are you a senior?
    #are you a veteran?
    return

#mainloop
orderagain="y"
while(orderagain=="y"):
    #iteration 1 - popcorn
    subtotal=0
    order=[]                            #order will store the user's order



choice, price = orderItem3Option("drink",["s","m","l"],[1,2,3]) 
subtotal+=price
order.append(choice)
print(f"subtotal: ${subtotal}")

choice, price = orderItem3Option("drink",["s","m","l"],[1,2,3]) 
subtotal+=price
order.append(choice)
print(f"subtotal:{subtotal:.2f}")


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
