import random

classroom=['bill','bo','baggins','brett','brayden']
subjects=['math','physics','lunch','cs','government']
#parrallel list = each index correlates to the other


for i in range(5):
    print(f"{classroom[i]}'s favorite class is {subjects[i]}")
#For var in my sequence. In this case my squence is a range(number of items in the classroom)
for i in range(len(classroom)):
    print(f"{classroom[i]}'s favorite class is {subjects[i]}")
    

first=["jim","john","jo","jon","james","jared","jarrot","j"]
last=["bo","smith","robbert","snow","cameron","diamon","orleans","k"]
print()
for i in range(len(first)): 
    print(f"{first[i]}.{last[i]}@stu.evsck12.com") 

#count how many "a"s are in "banana"

word,letter = "mississippi", "s"
count=0
for eachLetter in word:
    if eachLetter == letter:
     count +=1
print(count)

#replace each vowel in "McDonald's Play Place" with a "*"

word = "McDonald's Play Place"
for eachLetter in word:
    if eachLetter in "aeiou":
        print("*",end="")
    elif eachLetter == "y" and random.randint(0,1) == 1:
        print("*",end="")
    else:
        print(eachLetter,end="")




