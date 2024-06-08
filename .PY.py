class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'
    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')
        print('-' * (self.cols * 2 + 1))
    def is_valid_location(self, col):
        return self.board[0][col] == ' '
    def get_next_open_row(self, col):
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == ' ':
                return row
    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece
    def winning_move(self, piece):
        # Check horizontal locations for win
        for c in range(self.cols - 3):
            for r in range(self.rows):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        for c in range(self.cols):
            for r in range(self.rows - 3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
        for c in range(self.cols - 3):
            for r in range(self.rows - 3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True
        for c in range(self.cols - 3):
            for r in range(3, self.rows):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True
    def play(self):
        game_over = False
        self.print_board()
        while not game_over:
            col = int(input(f"Player {self.current_player}, make your selection (0-{self.cols-1}): "))
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                self.drop_piece(row, col, self.current_player)
                if self.winning_move(self.current_player):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    game_over = True
                else:
                    self.print_board()
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Invalid selection. Try again.")
if __name__ == "__main__":
    game = ConnectFour()
    game.play()
