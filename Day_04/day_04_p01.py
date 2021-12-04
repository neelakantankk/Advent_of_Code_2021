def parse_board(board):
    int_board = []
    for line in board.split("\n"):
        int_board.extend(int(x) for x in line.split())

    return int_board

def check_num(board,num):
    try:
        index = board.index(num)
        board[index] = 0
        return board
    except ValueError:
        return board

def is_complete_rows(board):
    for i in range(0,len(board)-5,5):
        row = board[i:i+5]
        if sum(row) == 0:
            return True
    return False

def is_complete_columns(board):
    for i in range(0,5):
        col = [board[i+j] for j in range(0,25,5)]
        if sum(col) == 0:
            return True
    return False

def get_winner(boards):
    for board in boards:
        if is_complete_rows(board) or is_complete_columns(board):
            return board

def main():
    with open('input','r') as infile:
        called_numbers = [int(x) for x in infile.readline().strip().split(",")]
        boards = [parse_board(x.strip()) for x in infile.read().split("\n\n")]

    for num in called_numbers[0:5]:
        boards = [check_num(board,num) for board in boards]

    winner = get_winner(boards)


    if winner is None:
        for num in called_numbers[5:]:
            boards = [check_num(board,num) for board in boards]
            winner = get_winner(boards)
            if winner is not None:
                final_num = num
                break

    sum_of_unmarked_rows = sum(winner)

    print(final_num * sum_of_unmarked_rows)


if __name__ == '__main__':
    main()

