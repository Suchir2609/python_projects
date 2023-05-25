import random

from hangman_logo import stages

from hangman_logo import logo
print(logo)

from words import word_list
# random_int = random.randint(0,2)
word = random.choice(word_list)

# print(f'Pssst, the solution is {word}.')

answer = []
lives = 6

for i in word:
    answer.append('_')

while '_' in answer:
    user_input = input("guess a letter: ").lower()
    if user_input in answer:
         print(f"you have already guessed {user_input}")

    for i in range(len(word)):
        letter = word[i]
        if user_input == letter:
            answer[i] = letter
    if user_input not in word:
        print(f"you guessed {user_input}, it is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            print("\nyou lose")
            print(f"the answer was {word}")
            break

    print(stages[lives])
    print(f"{''.join(answer)}")
    if '_' not in answer:
        print("you win")


# print("you win")
