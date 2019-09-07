import random
import os

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


secret_word = load_word()
secret_word_to_list = []  # This separates the letters into a list
secret_word_to_dashes = []  # Changes letters to dashes
all_letters_option = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']

for ch in secret_word:
    secret_word_to_list.append(ch)

for ch in secret_word:
    secret_word_to_dashes.append("-")

number_of_guesses = len(secret_word)
print("Welcome to Spaceman. You have " + str(number_of_guesses) + " guesses to choose all the correct letters in the secret word.")
print("Guess the secret word: " + ''.join(secret_word_to_dashes))

while number_of_guesses > 0:
    print('=================================================')
    user_input = input("Guess a letter: ")

    guessed_correct_character_index = []

    for i in range(len(secret_word_to_list)):
        if secret_word_to_list[i] == user_input:
            guessed_correct_character_index.append(i)

    if user_input in secret_word:
        print("Great! Your chosen letter is in the secret word!")
        number_of_guesses = number_of_guesses
    else:
        print("Yikes. Your chosen letter is not in the secret word.")
        number_of_guesses -= 1

    if user_input in all_letters_option:
        all_letters_option.remove(user_input)
        all_letters_updated = ''.join(all_letters_option)
        print("Letters left to guess: " + all_letters_updated)

    print('Number of guesses left: ' + str(number_of_guesses))

    for index in guessed_correct_character_index:
        secret_word_to_dashes[index] = user_input

    convert_answer_string = ''.join(secret_word_to_dashes)
    print(convert_answer_string)

    if convert_answer_string == secret_word:
        print("Congratulations! You guessed all of the letters in the secret word. You win")
        break

if number_of_guesses == 0:
    print("You are out of guesses. The secret word was " + secret_word + ". You lose.")