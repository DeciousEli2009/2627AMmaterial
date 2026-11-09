
'''Below is the order of operations for how to lineup code.'''
#import functions from anotehr file
from DistanceConversion import * #* is everything
#from DistanceConversion f(x) 


'''import example''' #imports always go first

#global variables/objects
menu = '''
    in to ft (if)           mph to kph (mk)
    ft to in (fi)           kph to mph (km)

    tbsp to tsp (tbts)      lbs to kg (lk)
    tsp to tbsp (tstb)      kg to lbs (kl)

    c to f (cf)             oz to cups (oc)
    f to c (fc)             cups to oz (co)

    stop (stop)

What would you like to do?
'''

#f(x)

#mainloop
user=input(menu)

while(user!="stop"):
    #algo
    if user == "if":
        print(in2ft(float(input("inches: "))))
    elif user == "fi":
        pass            #pass to the next iteration
    elif user == "mk":
        pass            #pass works as a great placeholder
    elif user == "km":
        pass
    elif user == "cf":
        print(c2f(float(input("Celcius: "))))
        pass
    elif user == "fc":
        pass
    elif user == "oc":
        pass
    elif user == "co":
        pass
    elif user == "lk":
        pass
    elif user == "kl":
        pass
    elif user == "tbts":
        pass
    elif user == "tstb":
        pass

    else:
        print("Im sorry I didnt understand that")
    user = input(menu)



