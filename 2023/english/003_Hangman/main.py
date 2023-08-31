import random
import os #it helps cleaning the previous stage
from hangman_words import word_list
from hangman_art import stages, logo
# from hangman_art import logo (I could import the logo by itself but it is better to import diferent things separating them with commas if they are in the same file)

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear') #with this code the game would clean the previous stage

    if guess in display:
        print(f"You already choose the letter {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

        print(f"The letter {guess} is not in the word. You lose a life")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])