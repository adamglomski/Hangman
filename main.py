import os
import random


def welcome_message():
    print('Witaj w grze WISIELEC.')


def get_start_decision():
    while True:
        wanna_play = input('Do you want to play? Type [Y/N]\n')
        if wanna_play in ('Y', 'y', ''):
            return True
        if wanna_play in ('N', 'n'):
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
    temp = 'X'*len(word)
    return temp


def get_word_lenght(word):
    return len(word)


def tries_left_amount(word, counter):
    amount = get_word_lenght(word) + 1 - counter
    return amount


def print_tries_left_amount(word, counter):
    print(f'Pozostało: {tries_left_amount(word, counter)} prób...')


def game_start_message():
    print('Zaczynajmy! Odgadnij poniższe hasło:')


def player_answer():
    while True:
        player_input = input().upper()
        if len(player_input) == 1 and player_input.isalpha():
            return player_input
        elif player_input.isalnum():
            print('The character must be a letter!')
            continue
        elif player_input == "":
            print('You must insert something!')
        else:
            print('Insert one character only!')
            continue


def check_literals(word, literal):
    if literal in word:
        counter = word.count(literal)
        print(f"Nice try! The amount of letter '{literal}' in our word: {counter}")


def word_after_guess(word, last_word_guessed, literal):
    word_list = list(word)
    word_after_guess_list = list(last_word_guessed)

    for i in range(len(word)):
        if word_list[i] == literal:
            word_after_guess_list[i] = literal

    word_partially_guessed = "".join(word_after_guess_list)
    return word_partially_guessed


def print_word_after_guess(word):
    print('Keep going! The word looks like this now:', word)


def game():
    tries_counter = 0
    game_start_message()
    generator = random_word_generator()
    the_word = next(generator)
    word_hidden = give_word_hidden(the_word)
    print(word_hidden)

    while 'X' in word_hidden:
        print_tries_left_amount(the_word, tries_counter)
        player_input = player_answer()
        check_literals(the_word, player_input)
        word_hidden = word_after_guess(the_word, word_hidden, player_input)
        print_word_after_guess(word_hidden)
        tries_counter += 1

    else:
        print('Contratulations! You won!')


# Starting the game here

welcome_message()

if get_start_decision():
    game()

else:
    input('Press any key to quit...')
