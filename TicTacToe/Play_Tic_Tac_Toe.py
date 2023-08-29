import os
import sys
import random

class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def is_valid_move(self, x, y):
        if x < 0 or x >= 3 or y < 0 or y >= 3:
            return False
        if self.board[3 * y + x] != ' ':
            return False
        return True

    def make_move(self, x, y, player):
        if not self.is_valid_move(x, y):
            return False
        self.board[3 * y + x] = player
        return True

    def get_winner(self):
        for row in range(3):
            if self.board[row * 3] == self.board[row * 3 + 1] == self.board[row * 3 + 2] != ' ':
                return self.board[row * 3]
        for col in range(3):
            if self.board[col] == self.board[col + 3] == self.board[col + 6] != ' ':
                return self.board[col]
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        return None

    def is_full(self):
        return not any(cell == ' ' for cell in self.board)

    def minimax(self, player):
        winner = self.get_winner()
        if winner:
            return {'X': -1, 'O': 1, None: 0}[winner]
        if self.is_full():
            return 0

        best_value = float('inf') if player == 'O' else float('-inf')
        for x in range(3):
            for y in range(3):
                if not self.is_valid_move(x, y):
                    continue
                self.make_move(x, y, player)
                value = self.minimax('O' if player == 'X' else 'X')
                self.make_move(x, y, ' ')
                if player == 'O':
                    best_value = min(best_value, value)
                else:
                    best_value = max(best_value, value)
        return best_value

    def get_best_move(self):
        best_value = float('-inf')
        best_move = None
        for x in range(3):
            for y in range(3):
                if not self.is_valid_move(x, y):
                    continue
                self.make_move(x, y, 'X')
                value = self.minimax('O')
                self.make_move(x, y, ' ')
                if value > best_value:
                    best_value = value
                    best_move = (x, y)
        return best_move


# def main():
#     game = TicTacToe()
#     player = 'X'
#     while True:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         game.print_board()
#         winner = game.get_winner()
#         if winner:
#             print(f'Player {winner} wins!')
#             break
#         if game.is_full():
#             print("It's a tie!")
#             break

#         if player == 'X':
#             x, y = game.get_best_move()
#             game.make_move(x, y, player)
#         else:
#             x, y = None, None
#             while not game.is_valid_move(x, y):
#                 try:
#                     move = input('Enter your move (1-9): ')
#                     if len(move) == 0:
#                         print("Invalid input. Please enter a number between 1 and 9.")
#                         continue
#                     move = int(move) - 1
#                     x, y = move % 3, move // 3
#                 except (ValueError, IndexError):
#                     print("Invalid input. Please enter a number between 1 and 9.")
#                     continue
#             game.make_move(x, y, player)

#         player = 'O' if player == 'X' else 'X'

# if __name__ == '__main__':
#     main()

def main():
    game = TicTacToe()
    player = 'X'
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        game.print_board()

        if player == 'X':
            x, y = game.get_best_move()
            game.make_move(x, y, player)
            player = 'O'  # Switch to human player
        else:
            x, y = None, None
            while not game.is_valid_move(x, y):
                try:
                    move = input('Enter your move (1-9): ')
                    if len(move) == 0:
                        print("Invalid input. Please enter a number between 1 and 9.")
                        continue
                    move = int(move) - 1
                    x, y = move % 3, move // 3
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue
            game.make_move(x, y, player)
            player = 'X'  # Switch to AI player

        winner = game.get_winner()
        if winner or game.is_full():
            break

    os.system('clear')
    game.print_board()
    if winner:
        print(f'Player {winner} wins!')
    else:
        print("It's a tie!")

if __name__ == '__main__':
    main()
