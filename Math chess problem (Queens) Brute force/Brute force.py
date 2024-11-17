
def convert_to_chess_notation(position, board_size):
    column_letter = chr(ord('A') + position // board_size)
    row_number = position % board_size + 1
    return "{}{}".format(column_letter, row_number)


def place_queens(n):
    # Initialize a counter variable
    move_count = 1

    with open("Results.txt", "a") as f:
        f.write("Trying solutions for {}x{} board:\n".format(n, n))
    i = j = k = l = 1
    temp_i = i
    temp_j = j
    temp_k = k
    temp_l = l
    for i in range(n * n):
        for j in range(i + 1, n * n):
            for k in range(j + 1, n * n):
                for l in range(k + 1, n * n):
                    for m in range(l + 1, n * n):
                        if (temp_i !=i and move_count != 1):
                            with open("Results.txt", "a") as f:
                                if (move_count / 10 < 1):
                                    with open("Results.txt", "a") as f:
                                        f.write("     {}) ".format(move_count))
                                elif (move_count / 10 < 10):
                                    with open("Results.txt", "a") as f:
                                        f.write("    {}) ".format(move_count))
                                elif (move_count / 10 < 100):
                                    with open("Results.txt", "a") as f:
                                        f.write("   {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write("  {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write(" {}) ".format(move_count))
                                else:
                                    with open("Results.txt", "a") as f:
                                        f.write("{}) ".format(move_count))
                            move_count += 1
                            with open("Results.txt", "a") as f:
                                f.write("-")
                            j = board_size * board_size - 4
                            k = board_size * board_size - 3
                            l = board_size * board_size - 2
                            m = board_size * board_size - 1
                            queens = [i, j, k, l, m]
                            chess_notation_queens = [convert_to_chess_notation(q, n) for q in queens]
                            with open("Results.txt", "a") as f:
                                f.write("Trying cells: {}; ".format(', '.join(chess_notation_queens)))
                            if is_board_covered(n, queens):
                                with open("Results.txt", "a") as f:
                                    f.write("\n")
                                    f.write("THIRD PART. Results\n")
                                    f.write("Solution found: {}\n".format(', '.join(chess_notation_queens)))
                            j = i + 1
                            k = j + 1
                            l = k + 1
                            m = l + 1

                        if (temp_j !=j and move_count != 1):
                            with open("Results.txt", "a") as f:
                                if (move_count / 10 < 1):
                                    with open("Results.txt", "a") as f:
                                        f.write("     {}) ".format(move_count))
                                elif (move_count / 10 < 10):
                                    with open("Results.txt", "a") as f:
                                        f.write("    {}) ".format(move_count))
                                elif (move_count / 10 < 100):
                                    with open("Results.txt", "a") as f:
                                        f.write("   {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write("  {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write(" {}) ".format(move_count))
                                else:
                                    with open("Results.txt", "a") as f:
                                        f.write("{}) ".format(move_count))
                            move_count += 1
                            with open("Results.txt", "a") as f:
                                f.write("--")
                            k = board_size * board_size - 3
                            l = board_size * board_size - 2
                            m = board_size * board_size - 1
                            queens = [i, j, k, l, m]
                            chess_notation_queens = [convert_to_chess_notation(q, n) for q in queens]
                            with open("Results.txt", "a") as f:
                                f.write("Trying cells: {}; ".format(', '.join(chess_notation_queens)))
                            if is_board_covered(n, queens):
                                with open("Results.txt", "a") as f:
                                    f.write("\n")
                                    f.write("THIRD PART. Results\n")
                                    f.write("Solution found: {}\n".format(', '.join(chess_notation_queens)))
                            k = j + 1
                            l = k + 1
                            m = l + 1

                        if (temp_k !=k and move_count != 1):
                            with open("Results.txt", "a") as f:
                                if (move_count / 10 < 1):
                                    with open("Results.txt", "a") as f:
                                        f.write("     {}) ".format(move_count))
                                elif (move_count / 10 < 10):
                                    with open("Results.txt", "a") as f:
                                        f.write("    {}) ".format(move_count))
                                elif (move_count / 10 < 100):
                                    with open("Results.txt", "a") as f:
                                        f.write("   {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write("  {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write(" {}) ".format(move_count))
                                else:
                                    with open("Results.txt", "a") as f:
                                        f.write("{}) ".format(move_count))
                            move_count += 1
                            with open("Results.txt", "a") as f:
                                f.write("---")
                            l = board_size * board_size - 2
                            m = board_size * board_size - 1
                            queens = [i, j, k, l, m]
                            chess_notation_queens = [convert_to_chess_notation(q, n) for q in queens]
                            with open("Results.txt", "a") as f:
                                f.write("Trying cells: {}; ".format(', '.join(chess_notation_queens)))
                            if is_board_covered(n, queens):
                                with open("Results.txt", "a") as f:
                                    f.write("\n")
                                    f.write("THIRD PART. Results\n")
                                    f.write("Solution found: {}\n".format(', '.join(chess_notation_queens)))
                            l = k + 1
                            m = l + 1

                        if (temp_l !=l and move_count != 1):
                            with open("Results.txt", "a") as f:
                                if (move_count / 10 < 1):
                                    with open("Results.txt", "a") as f:
                                        f.write("     {}) ".format(move_count))
                                elif (move_count / 10 < 10):
                                    with open("Results.txt", "a") as f:
                                        f.write("    {}) ".format(move_count))
                                elif (move_count / 10 < 100):
                                    with open("Results.txt", "a") as f:
                                        f.write("   {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write("  {}) ".format(move_count))
                                elif (move_count / 10 < 1000):
                                    with open("Results.txt", "a") as f:
                                        f.write(" {}) ".format(move_count))
                                else:
                                    with open("Results.txt", "a") as f:
                                        f.write("{}) ".format(move_count))
                            move_count += 1
                            with open("Results.txt", "a") as f:
                                f.write("----")
                            m = board_size * board_size - 1
                            queens = [i, j, k, l, m]
                            chess_notation_queens = [convert_to_chess_notation(q, n) for q in queens]
                            with open("Results.txt", "a") as f:
                                f.write("Trying cells: {}; ".format(', '.join(chess_notation_queens)))
                            if is_board_covered(n, queens):
                                with open("Results.txt", "a") as f:
                                    f.write("\n")
                                    f.write("THIRD PART. Results\n")
                                    f.write("Solution found: {}\n".format(', '.join(chess_notation_queens)))
                            m = l + 1

                        if (move_count / 10 < 1):
                            with open("Results.txt", "a") as f:
                                f.write("     {}) ".format(move_count))
                        elif (move_count / 10 < 10):
                            with open("Results.txt", "a") as f:
                                f.write("    {}) ".format(move_count))
                        elif (move_count / 10 < 100):
                            with open("Results.txt", "a") as f:
                                f.write("   {}) ".format(move_count))
                        elif (move_count / 10 < 1000):
                            with open("Results.txt", "a") as f:
                                f.write("  {}) ".format(move_count))
                        elif (move_count / 10 < 1000):
                            with open("Results.txt", "a") as f:
                                f.write(" {}) ".format(move_count))
                        else:
                            with open("Results.txt", "a") as f:
                                f.write("{}) ".format(move_count))

                        with open("Results.txt", "a") as f:
                            f.write("-----")
                        temp_i = i
                        temp_j = j
                        temp_k = k
                        temp_l = l
                        move_count += 1  # Increment the counter
                        queens = [i, j, k, l, m]
                        chess_notation_queens = [convert_to_chess_notation(q, n) for q in queens]
                        with open("Results.txt", "a") as f:
                            f.write("Trying cells: {}; ".format(', '.join(chess_notation_queens)))
                        if is_board_covered(n, queens):
                            with open("Results.txt", "a") as  f:
                                f.write("\n")
                                f.write("THIRD PART. Results\n")
                                f.write("Solution found: {}\n".format(', '.join(chess_notation_queens)))
                            # Return the counter along with queens
                                return queens, move_count

        with open("Results.txt", "a") as f:
            f.write("Solution not found for a {}x{} board\n".format(n, n)) # This should never pop up as it's restricted to go above 10x10

        # Return None if no solution found, along with the final move count
    return queens, move_count




def is_board_covered(n, queens):
    board = [[0] * n for _ in range(n)]
    for q in queens:
        row, col = q // n, q % n
        for i in range(n):
            board[i][col] = 1  # Marking columns
            board[row][i] = 1  # Marking rows
            if 0 <= row - i < n and 0 <= col - i < n:
                board[row - i][col - i] = 1  # Marking top-left to center diagonal
            if 0 <= row + i < n and 0 <= col + i < n:
                board[row + i][col + i] = 1  # Marking bottom-right to center diagonal
            if 0 <= row - i < n and 0 <= col + i < n:
                board[row - i][col + i] = 1  # Marking top-right to center diagonal
            if 0 <= row + i < n and 0 <= col - i < n:
                board[row + i][col - i] = 1  # Marking bottom-left to center diagonal
    covered = all(all(row) for row in board)
    if covered:
        with open("Results.txt", "a") as f:
            f.write("Entire board attacked by queens: Yes\n")
    else:
        with open("Results.txt", "a") as f:
            f.write("Entire board attacked by queens: No\n")
    return covered


def print_board(n, queens):
    # Create a dictionary to map row indices to letters
    row_letters = {i: chr(ord('A') + i) for i in range(n)}

    with open("Results.txt", "a") as f:
        f.write("First solution found for a {}x{} board:\n".format(n, n))

        # Write the top border to the file
        f.write("  " + "-" * (4 * n + 1) + "\n")

        # Write the rows to the file
        for row_idx in range(n):
            # Calculate the row label (letter)
            row_label = row_letters[row_idx]

            # Write the row label and vertical border to the file
            f.write(row_label + " | ")

            # Write the cells in the row to the file
            for col_idx in range(n):
                cell = ' ' if (row_idx + col_idx) % 2 == 0 else ' '
                if row_idx * n + col_idx in queens:
                    # Add 'Q' followed by the queen number
                    queen_number = queens.index(row_idx * n + col_idx) + 1
                    cell = 'Q' + str(queen_number)
                f.write(cell + " | ")

            # Move to the next row in the file
            f.write("\n  " + "-" * (4 * n + 1) + "\n")

        # Write the column labels (numbers) to the file
        f.write("    ")
        for col_idx in range(1, n + 1):
            f.write(str(col_idx).ljust(3) + " ")
        f.write("\n\n")




7
def print_chessboard(board_size, f):
    # Calculate the width of each cell
    cell_width = 3

    # Calculate the total width of the board (excluding row labels)
    board_width = cell_width * board_size

    # Write the top border to the file
    f.write("  " + "-" * (board_width + board_size + 1) + "\n")

    # Write the rows to the file
    for row in range(board_size):
        # Calculate the row label (letter)
        row_label = chr(65 + row)

        # Write the row label and vertical border to the file
        f.write(row_label + " | ")

        # Write the cells in the row to the file
        for col in range(board_size):
            if (row + col) % 2 == 0:
                f.write(" " * (cell_width - 1) + "| ")
            else:
                f.write(" " * (cell_width - 1) + "| ")

        # Move to the next row in the file
        f.write("\n  " + "-" * (board_width + board_size + 1) + "\n")

    # Write the column labels (numbers) to the file
    f.write("  ")
    for col in range(1, board_size + 1):
        f.write(str(col).rjust(cell_width) + " ")
    f.write("\n\n")




if __name__ == "__main__":
    with open("Results.txt", "w") as f:
        pass
    board_size = int(input("Choose the chessboard size: "))

    if board_size < 5 or board_size > 9:
        print("Error: Chessboard must be between 5x5 and 9x9.")
    else:
        intro_text = """
DESCRIPTION
Place 5 Queens in a N x N chessboard in a way where every cell would either be attacked or occupied by a queen.
Find the first solution
Try it with 3 tests: N = 8, 7, 9.
https://en.wikipedia.org/wiki/Mathematical_chess_problem.

SOLUTION:
Brute force method by pushing queens forward cell by cell until the solution to
the problem is found.

LIMITATIONS:
The program will work best with integers N between 7 and 9.
The program will cut itself off as soon as it finds the first solution.
Program is restricted to only work with integers N between 5 and 9
The progam will not work if you put in anything else other than an integer.

FIRST PART. Data.

1) Board size: {}x{}.
2) Number of queens: 5.
3) Queen starting coordinates: A1, A2, A3, A4, A5.
4) The amount of dashes (-) indicate which queen is moving in that step.
    """.format(board_size, board_size)

    with open("Results.txt", "a") as f:
        f.write(intro_text)
        f.write("\n")
        print_chessboard(board_size, f)
        f.write("ANTRA DALIS. Vykdymas.\n")

    queens, move_count = place_queens(board_size)
    with open("Results.txt", "a") as f:
        f.write("\n")
        f.write("Amount of iterations: {}.\n".format(move_count-1))
        f.write("\n")
    print_board(board_size, queens)
