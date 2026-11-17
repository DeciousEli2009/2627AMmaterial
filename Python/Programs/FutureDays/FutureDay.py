print("Hello!!! I am Eli Decoius and this is my day calculator!!!! I hope you enjoy!!!!")

week = ["Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday"]

print()
#Asks user the day and stores it
today = int(input("To start, tell me what day it is today (Sunday is 0, Saturday is 6): "))
later = int(input("Alright. How many days after today do you want to calculate? "))


#for loop that basically makes it to were idc what the number is bc it loops the 7 days
for time in range(later):
    today += 1
    if today == 7:
        today = 0

print("\n"*10)
print(f"In {later} day(s) it will be {week[today]}")






























