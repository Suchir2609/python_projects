import random

print("Welcome to number guessing game \nI'm thinking of a number between 1 and 100")
number = random.randint(0,100)
# print(f"answer : {number}")
difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    chances = 10
elif difficulty == "hard":
    chances = 5
for lives in range(0,chances):
    print(f"you have {chances-lives} attempts remaining to guess the number")
    guess = int(input("make aa guess: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    elif guess == number:
        print("You win")
        break
    if lives == chances-1:
        print("you ran out of guesses, you lose")
