from random import sample, choice

class Square():
    """ a square can either be a bomb, a hint (if next to a bomb), or blank"""
    def __init__(self, type):
        self.type = type
        

class Board():
    def __init__(self, size, m):
        self.size = size
        self.mines = m
        self.mine_locations = []
        self.grid = [[]*self.size]*self.size

    def reset_board(self):
        self.grid = [[0]*self.columns]*self.rows

    def create_mines_locations(self):
        for m in range(self.mines):
            self.mine_locations.append( sample(range(self.size), 2) )
        print(self.mine_locations)

    def insert_mines(self):
        for mine in self.mine_locations:
            x = mine[0]
            y = mine[1]
            # print(x,y)
            self.grid[x][y] = "B"

    def reveal(self):
        for row in range(self.size):
            print(self.grid[row])


def main():
    myboard = Board(4, 1)
    # myboard.reset_board()
    myboard.reveal()

    myboard.create_mines_locations()
    myboard.insert_mines()
    myboard.reveal()

    # print(myboard.grid)

if __name__ == '__main__':
    main()
