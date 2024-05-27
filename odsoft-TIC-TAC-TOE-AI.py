import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check the column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def minimax(board, maximizer):
    if board.current_winner == 'X':
        return 1
    elif board.current_winner == 'O':
        return -1
    elif not board.empty_squares():
        return 0

    if maximizer:
        max_eval = -math.inf
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, False)
            board.board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, True)
            board.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval


def get_best_move(board):
    best_move = None
    best_eval = -math.inf
    for move in board.available_moves():
        board.make_move(move, 'X')
        eval = minimax(board, False)
        board.board[move] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move


def play_game():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    print("You are playing against Codsoft AI.")
    game.print_board_nums()
    print("Here is the board layout:")
    while game.empty_squares():
        human_square = None
        while human_square not in game.available_moves():
            try:
                human_square = int(input("Enter your move (0-8): "))
            except ValueError:
                print("Please enter a number between 0 and 8.")
        game.make_move(human_square, 'O')
        if game.winner(human_square, 'O'):
            game.print_board()
            print("Congratulations! You win!")
            break
        if not game.empty_squares():
            print("It's a tie!")
            break
        ai_square = get_best_move(game)
        game.make_move(ai_square, 'X')
        if game.winner(ai_square, 'X'):
            game.print_board()
            print("Codsoft AI wins! Better luck next time.")
            break
        game.print_board()


if __name__ == "__main__":
    play_game()
