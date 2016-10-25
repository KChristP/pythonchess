class Board:
    height, width = 8, 8
    rows_with_starting_pieces = [0, 1, 6, 7]
    def __init__(self):
        self.board = [[None for x in range(self.height)] for y in range(self.width)]
        for x in self.rows_with_starting_pieces:
            for y in range(self.width):
                self.board[x][y] = Piece()

    def move_piece(start_pos, end_pos):
        erow, ecol = end_pos
        srow, scol = start_pos
        if all(start_pos)
        if self.board[erow][ecol] == None
            self.board[erow][ecol] = self.board[srow][scol]
            self.board[srow][scol] = None


    def fname(self):
        print self.board


class Piece(object):
    def __init__(self):
        self.hi = "hi"


a = Board()
a.fname()
