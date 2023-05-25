import random
from art import logo
print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10]
user_cards=[]
comp_cards=[]

for card in range(2):
    user_cards.append(random.choice(cards))
user_score = sum(user_cards)
comp_cards.append(random.choice(cards))
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card: {comp_cards}")

should_continue = True
while should_continue:
    choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if choice == "y":
        user_cards.append(random.choice(cards))
        user_score = sum(user_cards)
        if user_score > 21:
            print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
            # print("you lose")
            break
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards}")
    elif choice == "n":
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        while sum(comp_cards)<18:
            comp_cards.append(random.choice(cards))
        print(f"computers final hand: {comp_cards}, final score: {sum(comp_cards)}")
        should_continue = False

if sum(user_cards) <= 21 and sum(comp_cards) <= 21:
    if sum(user_cards) < sum(comp_cards):
        print("You lose")
    elif sum(user_cards) > sum(comp_cards):
        print("You win")
    else:
        print("draw")
elif sum(user_cards) > 21:
    print("you lose")
elif sum(comp_cards) > 21:
    print("you win")


