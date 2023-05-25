# This is a sample Python script
from replit import clear

def highest_key(dictionary):
    highest_value = 0
    highest_key = ""
    for key in dictionary:
        value = dictionary[key]
        if value > highest_value:
            highest_value = value
            highest_key = key
    print(f"\nthe winner is {highest_key} with a bid of ${highest_value}")

print("welcome to secret auction program")

status = True
details = {}
while status == True:
    name = input("what is your name?\n")
    bid = int(input("what's your bid?: $"))
    details[name] = bid
    other_bidders = input("are there other bidders? type 'yes' or 'no': ")
    if other_bidders == "yes":
        clear()
    elif other_bidders == "no":
        status = False

highest_key(details)

