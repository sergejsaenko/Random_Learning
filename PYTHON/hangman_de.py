import random
import string
import os
from hangman_words_de import words
from hangman_visual import lives_visual_dict


def clean_console():
    os.system("clear")


def get_valid_word(words):
    # get random word from the possible words given
    word = random.choice(words)
    # while the word has speical characters, continue searching
    while "ä" in word or "-" in word or "ö" in word or "ü" in word or "ß" in word or " " in word:
        word = random.choice(words)
    # return valid word
    return word.upper()


def hangman():
    # returned word to use in main function
    word = get_valid_word(words)
    # sets the word letters to be used
    word_letters = set(word)
    # gets the normal alphabet with uppercase letters
    alphabet = set(string.ascii_uppercase)
    # for futuere used letters from the user so they get an overview
    used_letters = set()
    # how many lives the user has
    lives = 7

    clean_console()
    # getting user inputs and playing the game
    while len(word_letters) > 0 and lives > 0:
        # tells the user what letters they have used
        print(f"You have {lives} lives left and you have used the following letters: ", " ".join(
            used_letters))

        # show the user the silhouette of the word with "-"
        word_list = [
            letter if letter in used_letters else "-" for letter in word]
        print(lives_visual_dict[lives])
        print(f"Current word: ", " ".join(word_list))

        # user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            clean_console()
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                # takes one live away
                lives = lives-1
                print(f"Sorry! Your letter isn't in the word! You lost a live!")

        elif user_letter in used_letters:
            clean_console()
            print("Sorry! You already used that letter! Try again!")

        else:
            clean_console()
            print("This is not a valid letter! Try again!")

    # while-loop breaks if he found all letters:
    if lives == 0:
        clean_console()
        print(lives_visual_dict[lives])
        print(f"You died, sorry! The word was: {word}!")
    else:
        print(f"You have found the word: {word}!")


if __name__ == '__main__':
    hangman()
