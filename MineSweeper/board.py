from random import sample, choice


def create_board(num_rows, num_cols, num_mines):
    total_cells = num_rows * num_cols
    

class Board():
    def __init__(self, num_row, num_col, num_mines):
        self.rows = num_row
        self.columns = num_col
        self.mines = num_mines

