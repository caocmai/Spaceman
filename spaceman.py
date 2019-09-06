import random
import os

# def load_word():
#     f = open('words.txt', 'r')
#     words_list = f.readlines()
#     f.close()

#     # words_list = words_list[0].split(' ')
#     secret_word = random.choice(words_list)
#     return secret_word

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

secret_word = load_word()
secret_word_to_list = []  # This replaces letters to dashes
all_letters_option = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
secret_word_to_dashes = []  # Changes letters to dashes

for ch in secret_word:
    secret_word_to_list.append(ch)

for ch in secret_word:
    secret_word_to_dashes.append("-")

# print(secret_word_to_list)
# print(secret_word_to_dashes)

# def check_if_all_matches(convert_answer_string):
#     if convert_answer_string == secret_word:
#         print("You win")

number_of_guesses = 7
print("Welcome to Spaceman. You have 7 guesses to choose all the correct letters in the secret word.")
print("Guess the secret word: " + ''.join(secret_word_to_dashes))

while number_of_guesses > 0:
    print('=================================================')
    user_input = input("Guess a letter: ")

    compare_list = []

    for i in range(len(secret_word_to_list)):
        if secret_word_to_list[i] == user_input:
            compare_list.append(i)

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

    # this returns the index
    # print(compare_list)
    print('Number of guesses left: ' + str(number_of_guesses))
    # convert_answer_string = ''

    for index in compare_list:
        secret_word_to_dashes[index] = user_input

    convert_answer_string = ''.join(secret_word_to_dashes)
    # print(''.join(secret_word_to_dashes))
    print(convert_answer_string)

    if convert_answer_string == secret_word:
        print("Congratulations! You guessed all of the letters in the secret word. You win")
        break

    # print(secret_word_to_dashes)
    # print(''.join(secret_word_to_dashes))


if number_of_guesses == 0:
    print("You are out of guesses. The secret word is " + secret_word + ". You lose.")

# if user_input in secret_word_to_list:
#   print("in the word")
# else:
#   print("not in word")

#use find().