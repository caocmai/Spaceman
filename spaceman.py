import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

# Load secret word
secret_word = load_word()
number_of_guesses = len(secret_word)
all_letters_option = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']

# This separates the letters in secret word onto a list
secret_word_to_list = []
for ch in secret_word:
    secret_word_to_list.append(ch)

# Changes letters to dashes
secret_word_to_dashes = []
for ch in secret_word:
    secret_word_to_dashes.append("-")

print("Welcome to Spaceman. You have " + str(number_of_guesses) + " incorrect guesses to choose all the correct "
                                                                  "letters in the secret word.")
print("Guess the secret word: " + ''.join(secret_word_to_dashes))

# Program runs when guesses are greater than 0
while number_of_guesses > 0:
    print('===================================================================')
    user_input = input("Guess a letter: ")

    if len(user_input) > 1:
        print("Guess only one letter at a time!")
        user_input = input("Guess a letter: ")

    guessed_correct_character_index = []

# Checks if guessed letter in secret word, and adds the index of letter(s) in word
    if user_input in secret_word:
        for i in range(len(secret_word_to_list)):
            if secret_word_to_list[i] == user_input:
                guessed_correct_character_index.append(i)
        print("Great! Your chosen letter is in the secret word!")
        number_of_guesses = number_of_guesses
    else:
        print("Yikes. Your chosen letter is not in the secret word.")
        number_of_guesses -= 1

# Checks and displays letters left to guess
    if user_input in all_letters_option:
        all_letters_option.remove(user_input)
        all_letters_updated = ''.join(all_letters_option)
        print("Letters left to guess: " + all_letters_updated)

    print('Number of guesses left: ' + str(number_of_guesses))

# Using the index, populates the letters in the right place, and displays it out
    for index in guessed_correct_character_index:
        secret_word_to_dashes[index] = user_input

    convert_answer_string = ''.join(secret_word_to_dashes)
    print("Guess the secret word: " + convert_answer_string)

    if convert_answer_string == secret_word:
        print("Congratulations! You guessed all of the letters in the secret word. You won")
        break

# Player wins if all letters are guessed for the secret word
if number_of_guesses == 0:
    print("You are out of guesses. The secret word was " + secret_word + ". You lose.")