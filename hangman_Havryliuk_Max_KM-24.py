# Problem Set 2, hangman.py
# Name: Havryliuk Max
# Collaborators: None
# Time spent: 1 Night

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    if set(secret_word).issubset(set(letters_guessed)):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed, guess_try):
    letters_guessed.append(guess_try)
    finall = ''
    for letter in secret_word:
        if letter in letters_guessed:
            finall = finall + letter
        else:
            finall = finall + '_ '
    print(finall)


def get_available_letters(finall):
    available_letters = string.ascii_lowercase
    return available_letters.replace(finall, '')




def hangman(secret_word):
    letters_guessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('-' * 100)
    tries = 6
    warnings = 3
    while tries > 0:
        guess_try = input('Try to guess the letter that have secret word -  ').lower()
        print('-' * 100)

        if guess_try in secret_word and guess_try in letters_guessed:
            print('You have already tried this letter!')
            if warnings > 0:
                vowels = ['a', 'e', 'i', 'o', 'u', 'y']
                consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w']
                if guess_try in vowels:
                    warnings = warnings - 2
                    print("You have", tries, "attempts and", warnings, "warnings")
                elif guess_try in consonant:
                    warnings = warnings - 1
                    print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            elif warnings == 0:
                tries = tries - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
        elif len(guess_try) > 1:
            print('Warning! You can try only one letter at time')
            if warnings > 0:
                warnings = warnings - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            elif warnings <= 0:
                tries = tries - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters -', get_available_letters(guess_try))
        elif guess_try.isalpha() == False:
            print('Warning! It must be a letter!')
            if warnings > 0:
                warnings = warnings - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            elif warnings <= 0:
                tries = tries - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters -', get_available_letters(guess_try))
        elif guess_try in secret_word and guess_try not in letters_guessed:
            print('Good guess!')
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters - ' + get_available_letters(guess_try))
        elif guess_try not in secret_word:
            tries = tries - 1
            print('Oops! That letter is not in my word')
            print("You have", tries, "attempts and", warnings, "warnings")
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters -', get_available_letters(guess_try))

        if tries == 0:
            print('-' * 100)
            print('Sorry, you ran out of guesses. The word was else.')
            break
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print('-' * 100)
            print('Congratulations, you won!')
            break




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ', '')
    my_word_set = set(my_word)
    if len(my_word) == len(other_word):
        for i, underscore in enumerate(my_word):
            if underscore == "_":
                if other_word[i] in my_word_set:
                    return False
    else:
      return False
    return True

def show_possible_matches(my_word):
    possible_matches = list()
    for words in wordlist:
        if match_with_gaps(my_word, words):
            possible_matches.append(words)

    print(possible_matches)

def hangman_with_hints(secret_word):
    letters_guessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    print('-' * 50)
    tries = 6
    warnings = 3
    while tries > 0:
        guess_try = input('Try to guess the letter that have secret word -  ').lower()
        print('-' * 100)

        if '*' in guess_try:
            my_word = get_guessed_word(secret_word,letters_guessed,guess_try)
            print('Possible secret words:')
            show_possible_matches(my_word)
        elif guess_try in secret_word and guess_try in letters_guessed:
            print('You have already tried this letter!')
            if warnings > 0:
                vowels = ['a', 'e', 'i', 'o', 'u', 'y']
                consonant = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w']
                if guess_try in vowels:
                    warnings = warnings - 2
                    print("You have", tries, "attempts and", warnings, "warnings")
                elif guess_try in consonant:
                    warnings = warnings - 1
                    print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            elif warnings == 0:
                tries = tries - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
        elif len(guess_try) > 1:
            print('Warning! You can try only one letter at time')
            if warnings > 0:
                warnings = warnings - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            elif warnings <= 0:
                tries = tries - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters -', get_available_letters(guess_try))
        elif guess_try.isalpha() == False:
            print('Warning! It must be a letter!')
            if warnings > 0:
                warnings = warnings - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            elif warnings <= 0:
                tries = tries - 1
                print("You have", tries, "attempts and", warnings, "warnings")
                print('Available letters - ' + get_available_letters(guess_try))
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters -', get_available_letters(guess_try))
        elif guess_try in secret_word and guess_try not in letters_guessed:
            print('Good guess!')
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters - ' + get_available_letters(guess_try))
        elif guess_try not in secret_word:
            tries = tries - 1
            print('Oops! That letter is not in my word')
            print("You have", tries, "attempts and", warnings, "warnings")
            get_guessed_word(secret_word, letters_guessed, guess_try)
            print('Available letters -', get_available_letters(guess_try))

        if tries == 0:
            print('-' * 100)
            print('Sorry, you ran out of guesses. The word was else.')
            break
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print('-' * 100)
            print('Congratulations, you won!')
            break
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
