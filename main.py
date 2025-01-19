print("Welcome to Tic Tac Toe!\nUse num pad for playing and press Enter")
turn = 2
game_board = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n',
              '-----------', '\n', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ', '\n',
              '-----------', '\n', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
keys = {1: 1, 2: 5, 3: 9, 4: 15, 5: 19, 6: 23, 7: 29, 8: 33, 9: 37}
turn_sign = ["X", "O"]
used_cells = []

def check_win():
    win_conditions = [
        [keys[1], keys[2], keys[3]],
        [keys[4], keys[5], keys[6]],
        [keys[7], keys[8], keys[9]],
        [keys[1], keys[4], keys[7]],
        [keys[2], keys[5], keys[8]],
        [keys[3], keys[6], keys[9]],
        [keys[1], keys[5], keys[9]],
        [keys[3], keys[5], keys[7]]
    ]
    for condition in win_conditions:
        if game_board[condition[0]] == game_board[condition[1]] == game_board[condition[2]] != ' ':
            return True
    return False

while len(used_cells) < 9:
    print(''.join(game_board))
    try:
        num_entered = int(input("Enter a number (1-9): "))
        if num_entered in range(1, 10) and num_entered not in used_cells:
            game_board[keys[num_entered]] = turn_sign[turn % 2]
            used_cells.append(num_entered)
            if check_win():
                print(''.join(game_board))
                print(f"{turn_sign[turn % 2]} wins!")
                break
            turn += 1
        else:
            print("Invalid input or cell already used. Try again.")
    except ValueError:
        print("Please enter a valid number.")
else:
    print("It's a draw!")
