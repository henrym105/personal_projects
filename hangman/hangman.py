import stages as st
import words 
from art import text2art
import os


stages = st.get_stages()
rip = st.rip()

def clear():
    # Start by clearing the terminal so it looks nice
    # os.system('cls')      # uncomment if PC
    os.system('clear')      # uncomment if Mac


def hangman(word):
    wrong = 0
    answer = list(word)
    board = ["_"] * len(word)
    win = False
    prev_guesses = []

    clear()
    print("(c) Henry Marquardt, 2023\n")
    print(text2art("Welcome      to"))
    print(st.full())
    print(text2art("        Hangman"))

    print(f"A {len(word)}-letter word has been chosen at random. You have 7 guesses:")
    # print(" ".join(board))

    while wrong < len(stages) - 1:
        print("\n")
        print(stages[wrong])
        print(f"Used Letters: {', '.join(prev_guesses)}")
        guess = input("Guess a letter: ")
        if guess == "quit":
            break

        os.system('clear')

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
        print(text2art("You     Win!"))
        # print(f"The word is {word.upper()}.")
        print()
    else:
        clear()
        print(rip)
        print(text2art("You     Lose!"))
        print(f"The word was {word.upper()}.")
        print()

if __name__ == "__main__":    
    clear()
    hangman(words.food())
    while input("\n\nPress Enter to play or type 'quit': ").lower() != "quit":
        hangman(words.food())
