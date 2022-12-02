GRID_SIZE = 3


def create_grid(string):
    grid = []
    row_count = int(len(string) / GRID_SIZE)
    for i in range(row_count):
        grid.append(list(string[i * GRID_SIZE: i * GRID_SIZE + GRID_SIZE]))
    return grid


def empty_grid():
    grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    return grid


def print_grid(grid):
    print("-" * 9)
    for i in range(len(grid)):
        row = "| "
        for j in range(len(grid)):
            if grid[i][j] == "_":
                grid[i][j] = " "
            row += f"{grid[i][j]} "
        row += "|"
        print(row)
    print("-" * 9)


def get_rows_result(grid):
    rows_result = []
    for i in range(GRID_SIZE):
        count_x, count_o = 0, 0
        for j in range(GRID_SIZE):
            if grid[i][j] == "X":
                count_x += 1
            elif grid[i][j] == "O":
                count_o += 1
            elif grid[i][j] == "_":
                pass
        rows_result.append([count_x, count_o])
    return rows_result


def get_cols_result(grid):
    cols_result = []
    for j in range(GRID_SIZE):
        count_x, count_o = 0, 0
        for i in range(GRID_SIZE):
            if grid[i][j] == "X":
                count_x += 1
            elif grid[i][j] == "O":
                count_o += 1
        cols_result.append([count_x, count_o])
    return cols_result


def get_diagonal_results(grid):
    diagonal_results = []
    count_x, count_o = 0, 0
    for i in range(GRID_SIZE):
        if grid[i][i] == "X":
            count_x += 1
        elif grid[i][i] == "O":
            count_o += 1

    diagonal_results.append([count_x, count_o])

    count_x, count_o = 0, 0
    for i in range(GRID_SIZE):
        if grid[i][GRID_SIZE - i - 1] == "X":
            count_x += 1
        elif grid[i][GRID_SIZE - i - 1] == "O":
            count_o += 1

    diagonal_results.append([count_x, count_o])
    return diagonal_results


def check_empty_cells(grid):
    for row in grid:
        for c in row:
            if c == " ":
                return True
    return False


def count_three_x(list_results):
    count_three = 0
    for row in list_results:
        if row[0] == 3:
            count_three += 1
    return count_three


def count_three_o(list_results):
    count_three = 0
    for row in list_results:
        if row[1] == 3:
            count_three += 1
    return count_three


def count_x_o(grid):
    count_x, count_o = 0, 0
    for row in grid:
        for c in row:
            if c == "X":
                count_x += 1
            if c == "O":
                count_o += 1
    return count_x, count_o


def check_game_state(grid):
    rows_result = get_rows_result(grid)
    cols_result = get_cols_result(grid)
    diagonal_result = get_diagonal_results(grid)

    count_x_wins = count_three_x(rows_result) + count_three_x(cols_result) + count_three_x(diagonal_result)
    count_o_wins = count_three_o(rows_result) + count_three_o(cols_result) + count_three_o(diagonal_result)
    count_x, count_o = count_x_o(grid)

    if count_x_wins + count_o_wins > 1 or abs(count_x - count_o) >= 2:
        return "Impossible"
    elif count_x_wins == 1:
        return "X wins"
    elif count_o_wins == 1:
        return "O wins"
    elif check_empty_cells(grid):
        return "Game not finished"
    else:
        return "Draw"


def get_coordinates(grid):
    while True:
        user_input = input("Enter the coordinates: ").split()
        try:
            x = int(user_input[0])
            y = int(user_input[1])

            if x not in (1, 2, 3) or y not in (1, 2, 3):
                print("Coordinates should be from 1 to 3!")
                continue

            if grid[x - 1][y - 1] in ("X", "O"):
                print("This cell is occupied! Choose another one!")
                continue

            return x, y

        except ValueError:
            print("You should enter numbers!")


def main():
    grid = empty_grid()
    print_grid(grid)
    player_mark = "X"
    while True:
        x, y = get_coordinates(grid)
        grid[x - 1][y - 1] = player_mark
        if player_mark == "X":
            player_mark = "O"
        else:
            player_mark = "X"
        print_grid(grid)
        game_state = check_game_state(grid)
        if game_state not in "Game not finished":
            break
    print(game_state)


if __name__ == "__main__":
    main()
