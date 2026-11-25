print("Hello! This program sorts three numbers from least to greatest based from your input!! This program was made by Eli Decious. I hope you enjoy!!!!") 


a = int(input("enter first whole number: "))
b = int(input("Enter Second Whole Number: "))
c = int(input("Enter Third Whole Number: "))

if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)
