#Random selection of words to make game more interesting
import random
# We ill import clear at the button to not repeat every stage of the art of hangman, the console will clear and load where you left up. 
import os
#calling the list already saved under file hangman_words.py and importing all files needed 
from hangman_words import word_list
from hangman_art import stages, logo

#start randomizer funtion to sort the list and pick a random word to guess 
# 1 create a variable that holds the chosen_word and set the value to function random.choice and call the list
# 2 create a second variable that will determine the lenght of the word chosen and set the value to function len(chosen_word)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
givenLetter = [chosen_word[1]]

# Create a variable that will determine the amount of chances a player gets to guess the mistery word. When the chances END
end_of_game = False
live_numbers = 6

#import the logo saved in the hangman_art file by calling it to main

#Print the first s
print(logo)
print("Welcome to HANGMAN!, a word will be ramdonly chosen and must guess before running out of attempts! ")
print (stages[0])
print (f"Here is a clue the word contains {givenLetter} and it has {word_length} letters")



# Testing 1 print(f'Check the solution {chosen_word}.')
# Next we will be creating the blank spaces 
display = []
for _ in range(word_length):
    display += "_"
        #Start Looping through the game to guess the word use the varialble gameOver use the lower case function in the input hence letter casing is ignored  
while not end_of_game and live_numbers != 0 : #/////////////////////////////////////////////////////Added !=0 and "-" in chosen word 
    guess = input("Guess a letter: ").lower()
        #  if the player has guessed a valid letter print it and let the user know 
    os.system('cls')
    if guess in display:
      print(f"You have guessed: {guess}")
        #Checking the guessed letter position 
#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        live_numbers -= 1
        if live_numbers == 0:
            end_of_game = True
            print("Mwahhahaha, YOU HAD DIED!.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[live_numbers])

#OUTGRIDMODEL - DENISSE PEREZ RAMIREZ 5/27/2024

