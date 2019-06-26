import os
import random

#Define constant for hidden letters
hidden_letter = '_'

def welcome_message():
    print('Welcome in HANGMAN.')


def get_start_decision():
    while True:
        wanna_play = input('Do you want to play? Type [Y/N]\n')
        if wanna_play in ('Y', 'y', ''):
            return True
        if wanna_play in ('N', 'n'):
            return False
        continue


def want_another_word():
    while True:
        player_input = input('Do you want another word? Type [Y/N]\n')
        if player_input in ('Y', 'y', ''):
            return True
        if player_input in ('N', 'n'):
            return False
        continue


def random_word_generator():
    dictionary_file_name = 'dictionary.txt'
    dictionary_path = os.path.join(os.getcwd(), dictionary_file_name)
    temp_words_list = []

    with open(dictionary_path) as file:
        for line in file:
            word = line[:-1]
            if not word.isalpha():
                continue
            temp_words_list.append(word.upper())

    while True:
        random_word = random.choice(temp_words_list)
        yield random_word


def give_word_hidden(word):
    temp = hidden_letter*len(word)
    return temp


def tries_left_amount(word, counter):
    amount = len(word) + 3 - counter
    return amount


def print_tries_left_amount(word, counter):
    print(f'(Number of tries left: {tries_left_amount(word, counter)})')


def game_start_message():
    print('Let\'s start! Try to guess the following word (insert a character):')


def player_answer():
    while True:
        player_input = input().upper()
        if len(player_input) == 1 and player_input.isalpha():
            return player_input
        elif len(player_input) != 1:
            print('Insert one character only!')
        elif player_input.isalnum():
            print('The character must be a letter!')
            continue
        elif player_input == "":
            print('You must insert something!')
        else:
            print('I did not see that coming!   x_O')
            continue


def check_literals(word, literal):
    if literal in word:
        counter = word.count(literal)
        print(f"Good guess! The amount of letter '{literal}' in our word: {counter}")
        return True
    else:
        return False


def word_after_guess(word, last_word_guessed, literal):
    word_list = list(word)
    word_after_guess_list = list(last_word_guessed)

    for i in range(len(word)):
        if word_list[i] == literal:
            word_after_guess_list[i] = literal

    word_partially_guessed = "".join(word_after_guess_list)
    return word_partially_guessed


def print_word_after_guess(word):
    word_to_print_list = list(word)
    for i in range(len(word)):
        word_to_print_list[i] += ' '
    word_to_print = " ".join(word_to_print_list)
    print(f'{word_to_print}  ({len(word)} characters)')


def print_win(word):
    print('You won! The word we were looking for was:', word)


def game():
    game_start_message()
    tries_counter = 0
    lost_counter = 0
    generator = random_word_generator()
    the_word = next(generator)
    word_hidden = give_word_hidden(the_word)

    print_word_after_guess(word_hidden)
    print_tries_left_amount(the_word, lost_counter)

    while want_another_word():
        the_word = next(generator)
        word_hidden = give_word_hidden(the_word)

        print(f'New word for you:')
        print_word_after_guess(word_hidden)

    else:
        print('Let\'s continue then...')
        print_word_after_guess(word_hidden)

    while hidden_letter in word_hidden:

        if tries_left_amount(the_word, lost_counter) > 0:
            print_tries_left_amount(the_word, lost_counter)
            print('Insert a character:')

            player_input = player_answer()

            word_hidden = word_after_guess(the_word, word_hidden, player_input)

            check = check_literals(the_word, player_input)

            if not check:
                lost_counter += 1
                tries_counter += 1
                print('Nope! Try Again:')
                print_word_after_guess(word_hidden)
            else:
                tries_counter += 1
                print('Keep going! The word looks like this now:')
                print_word_after_guess(word_hidden)

        else:
            print('\nSorry, you lost this time! :(')
            print('The word was:')
            print_word_after_guess(the_word)
            return False

    else:
        print_win(word_hidden)
        print(f'Congratulations! You won in {tries_counter} tries!')
        return True
# Starting the game here

welcome_message()

games_counter = 0
win_count = 0
lost_count = 0

while get_start_decision():
    try:
        if game():
            win_count += 1
        else:
            lost_count += 1

        games_counter += 1

    except Exception as e:

        print('Error:', e)

else:
    print(f'You won {win_count} out of {games_counter} games (lost {lost_count}).')
    input('Press any key to quit...')
