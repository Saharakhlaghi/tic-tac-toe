def create():
    return [[' ' for _ in range(4)] for _ in range(4)]

def print_board(board):
    print("    1   2   3   4")
    print("  +---+---+---+---+")
    for x in range(len(board)):
        row_str = ' | '.join(board[x])
        print(f"{x + 1} | {row_str} |")
        print("  +---+---+---+---+")


def gather(board):
    lines = []
    lines.extend(board)
    columns = []
    for i in range(4):
        column = []
        for j in range(4):
            column.append(board[j][i])
        columns.append(column)
    lines.extend(columns)
    diag1 = []
    diag2 = []
    for i in range(4):
        diag1.append(board[i][i])
        diag2.append(board[i][3-i])
    lines.append(diag1)
    lines.append(diag2)
    return lines

def score(board):
    score = 0
    lines = gather(board)
    scores = {'X': {4: 20000, 3: 2000, 2: 200, 1: 20}, 'O': {4: -20000, 3: -800, 2: -50, 1: -20}}
    for line in lines:
        for player in ['X', 'O']:
            player_count = line.count(player)
            empty_count = line.count(' ')
            if player_count + empty_count == 4:
                if player_count == 4:
                    return scores[player][4]
                elif player_count in scores[player]:
                    score += scores[player][player_count]
    return score

def check_winner(board):
    lines = gather(board)
    for line in lines:
        if line[0] != ' ':
            is_same = True
            for cell in line:
                if cell != line[0]:
                    is_same = False
                    break
            if is_same:
                return line[0]
    return None

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True 

def best(board):
    best_move = None
    best_value = -float('inf')
    for i in range(4):
        for j in range(4):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_value = score(board)
                board[i][j] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move





def play():
    game_board = create()
    active_player = 'O'
    
    while True:
        print_board(game_board)  
        winner = check_winner(game_board)
        if winner:
            print(f"{winner} wins!")
            break
        if check_draw(game_board):
            print("It's a tie!")
            break
        if active_player == 'O':
            move_valid = False
            while not move_valid:
                user_input = input("Enter your move (row and column 1-4): ")
                try:
                    row, col = map(int, user_input.split())
                    if 0 <= row-1 < 4 and 0 <= col-1 < 4 and game_board[row-1][col-1] == ' ':
                        game_board[row-1][col-1] = 'O'
                        move_valid = True
                    else:
                        print("Invalid move! Try again.")
                except ValueError:
                    print("Please enter two numbers separated by a space.")
            active_player = 'X'
        else:
            print("Computer's turn:")
            optimal_move = best(game_board)
            if optimal_move:
                game_board[optimal_move[0]][optimal_move[1]] = 'X'
                print(f"Computer plays at {optimal_move[0]+1}, {optimal_move[1]+1}")
                active_player = 'O'
            else:
                print("No moves left!")
                break

play()
