print("Dope ass Sudoku solver. Enter your victim below:")
row1 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 1:")
    item = int(input())
    row1.append(item)
row2 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 2:")
    item = int(input())
    row2.append(item)
row3 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 3:")
    item = int(input())
    row3.append(item)
row4 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 4:")
    item = int(input())
    row4.append(item)
row5 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 5:")
    item = int(input())
    row5.append(item)
row6 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 6:")
    item = int(input())
    row6.append(item)
row7 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 7:")
    item = int(input())
    row7.append(item)
row8 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 8:")
    item = int(input())
    row8.append(item)
row9 = []
for i in range(1,10):
    print("Enter number in cell", i, "of row 9:")
    item = int(input())
    row9.append(item)

board = [row1, row2, row3, row4, row5,0
         0row6, row7, row8, row9]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)