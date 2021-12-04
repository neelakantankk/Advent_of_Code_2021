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

def get_winners(boards):
    winners = []
    for index, board in enumerate(boards):
        if is_complete_rows(board) or is_complete_columns(board):
            winners.append(board)
    return winners

def main():
    with open('input','r') as infile:
        called_numbers = [int(x) for x in infile.readline().strip().split(",")]
        boards = [parse_board(x.strip()) for x in infile.read().split("\n\n")]

    for num in called_numbers[0:5]:
        boards = [check_num(board,num) for board in boards]

    winners = []

    for num in called_numbers[5:]:
        winner = None
        final_num = num
        boards = [check_num(board,num) for board in boards]
        winners = get_winners(boards)
        for board in winners:
            boards.remove(board)
        if len(boards) == 0:
            final_num = num
            winner = winners[-1]
            break

    print(final_num * sum(winner))


if __name__ == '__main__':
    main()

