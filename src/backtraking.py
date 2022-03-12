def is_valid(row, col, queens):
    for r in range(row):
        if col == queens[r]:
            return False
        elif abs(col - queens[r] == abs(row - r)):
            return False
    return True


def place_queens(row, queens, n):
    if row == n:
        print(queens)
        return 1
    else:
        total_solns = 0
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col
                total_solns += place_queens(row + 1, queens, n)
        return total_solns


def n_queens(n):
    queens = [''] * n  # determinar cuantas reinas se quiere en el tableron
    row = 0
    return place_queens(row, queens, n)


n_queens(4)
