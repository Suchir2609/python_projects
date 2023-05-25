import random
from game_data import data
from art import vs,logo
print(logo)
number_A = random.randint(0,49)
points = 0
should_continue = True
while should_continue:
    print(f"compare A: {data[number_A]['name']},a {data[number_A]['description']},from {data[number_A]['country']}")

    print(vs)

    next = random.randint(0,49)
    print(f"Against B: {data[next]['name']},a {data[next]['description']},from {data[next]['country']}")

    answer = input("who has more followers? Type 'A' or 'B' ")
    print("\n")
    if data[number_A]['follower_count'] > data[next]['follower_count'] and answer == "A":
        points+=1
        print(f"You're right, current score = {points}")
    elif data[number_A]['follower_count'] > data[next]['follower_count'] and answer == "B":
        print(f"wrong answer, your total points are {points}")
        should_continue = False
    elif data[number_A]['follower_count'] < data[next]['follower_count'] and answer == "A":
        print(f"wrong answer, your total points are {points}")
        should_continue = False
    elif data[number_A]['follower_count'] < data[next]['follower_count'] and answer == "B":
        number_A = next
        points+=1
        print(f"You're right, current score = {points}")