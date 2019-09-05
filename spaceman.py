secret_word = "cat"
secret_word_list = [] # This is replaces letters to dashes
all_letters_option = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
list_start = []

for ch in secret_word:
    secret_word_list.append(ch)

for ch in secret_word:
    list_start.append("_")

print(secret_word_list)
print(list_start)


number_of_guesses = 7

# def check_if_all_matches(convert_answer_string):
#     if convert_answer_string == secret_word:
#         print("You win")


while number_of_guesses > 0:
    print('=============================================')
    user_input = input("Guess a letter: ")


    compare_list = []

    for i in range(len(secret_word_list)):
        if secret_word_list[i] == user_input:
            compare_list.append(i)

    if user_input in secret_word:
        print("Great! Your chosen letter is in the secret word!")
        number_of_guesses = number_of_guesses
    else:
        print("Sorry, your chosen letter is not in the secret word.")
        number_of_guesses -= 1

    if user_input in all_letters_option:
        all_letters_option.remove(user_input)
        all_letters_updated = ''.join(all_letters_option)
        print("Letters left to guess: " + all_letters_updated)

    # this returns the index
    print(compare_list)
    print('Number of guesses left: ')
    print(number_of_guesses)
    # convert_answer_string = ''

    for index in compare_list:
        list_start[index] = user_input

    convert_answer_string = ''.join(list_start)
    # print(''.join(list_start))

    print(convert_answer_string)

    if convert_answer_string == secret_word:
        print("Congratulations! You guessed all of the letters in the secret word. You win")
        break

    print("This is list start")
    print(list_start)
    # print(''.join(list_start))


if number_of_guesses == 0:
    print("You are out of guesses. The secret word is " + secret_word + ". You lose")

# if user_input in secret_word_list:
#   print("in the word")
# else:
#   print("not in word")

#use find().