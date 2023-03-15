import stages as st
import words 
from art import text2art
import os


stages = st.get_stages()

def hangman(word):
    wrong = 0
    answer = list(word)
    board = ["_"] * len(word)
    win = False
    prev_guesses = []

    # Clear the terminal so it looks nice
    os.system('cls')
    print(text2art("Welcome      to"))
    print(stages[-1])
    print(text2art("Hangman"))

    print(f"A {len(word)}-letter word has been chosen at random. You have 7 guesses:")
    # print(" ".join(board))

    while wrong < len(stages) - 1:
        print("\n")
        print(stages[wrong])
        print(f"Used Letters: {', '.join(prev_guesses)}")
        guess = input("Guess a letter: ")
        
        os.system('cls')

        while guess in prev_guesses:
            print(f"Used Letters: {', '.join(prev_guesses)}")
            guess = input(f"You already chose {guess.upper()}. Please enter another letter: ")
        if guess not in prev_guesses:
            prev_guesses.append(guess)        

        if guess not in answer:
            wrong += 1
        else:
            while guess in answer:
                here = answer.index(guess)
                board[here] = guess
                answer[here] = '$'        

        print("\n", " ".join(board), end='\r')

        if "_" not in board:
            win = True
            break

    if win:
        # Print a celebratory message
        print(text2art("You Win!"))
        # print(f"The word is {word.upper()}.")
        print()
    else:
        print(stages[-1])
        print(text2art("You Lose!"))
        print(f"The word was {word.upper()}.")
        print()

if __name__ == "__main__":
    hangman(words.random_word())
    while input("Press Enter to play again (q to quit): ").lower() != "q":
        hangman(words.random_word())
