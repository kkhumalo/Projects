#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    f = open(file_name, 'r')
    words = f.readlines()
    f. close()
    return words



def select_random_word(word):
    """
    TODO: Step 2 - select random word from list of file
    """

    random_word = word[random.randint(0,len(word)-1)]
    letter = random.randint(0,len(random_word)-2)
    print("Guess the word: " +random_word[ :letter] + "_" + random_word[letter+1: ]) 
    return random_word


def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    guess = input('Guess the missing letter: ')
    return guess

def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

