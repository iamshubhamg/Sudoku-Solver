def solve(S):
    # Find indexes with a zero value index
    t = []
    for i, s in enumerate(S):
        if s == 0:
            t.append(i)

    # Solver part. Run index p over the initial empty spaces
    # Going to the next free index is eq to incrementing p by one
    # Backtracking is then done by decrementing p
    p = 0
    while 0 <= p < len(t):
        # Find index and increment value by one
        i = t[p]
        S[i] += 1

        # If incrementing beyond 9, reset and backtrack
        if S[i] == 10:
            p -= 1
            S[i] = 0

        else:
            # Calculate cell information
            ri = i // 9
            ci = i % 9
            bi = (ri // 3)*3 + (ci // 3)

            # Check validity
            # Using for-else syntax. The else part is only run if the for loop is not broke
            for j, s in enumerate(S):
                # Different cell, but same value
                if i != j and s == S[i]:
                    # Calculate other cell information
                    rj = j // 9
                    cj = j % 9
                    bj = (rj // 3) * 3 + (cj // 3)
                    # If same row, col or block, break the loop. The insert number is not valid
                    if ri == rj or ci == cj or bi == bj:
                        break
            else:
                # Value at indes t[p] is valid. Go to the next empty index
                p += 1


def print_sudoku(S):
    print("-" * (9 * 2 + 4 * 2 - 1))
    for i, s in enumerate(S):
        if i % 3 == 0:
            print("| ", end="")
        print(s, end=" ")
        if i % 9 == 8:
            print("|")
            if i % 27 == 26:
                print("-" * (9 * 2 + 4 * 2 - 1))
            
if __name__ == "__main__":
    S = [5, 3, 0, 0, 7, 0, 0, 0, 0,
         6, 0, 0, 1, 9, 5, 0, 0, 0,
         0, 9, 8, 0, 0, 0, 0, 6, 0,
         8, 0, 0, 0, 6, 0, 0, 0, 3,
         4, 0, 0, 8, 0, 3, 0, 0, 1,
         7, 0, 0, 0, 2, 0, 0, 0, 6,
         0, 6, 0, 0, 0, 0, 2, 8, 0,
         0, 0, 0, 4, 1, 9, 0, 0, 5,
         0, 0, 0, 0, 8, 0, 0, 7, 9]
         
    solve(S)
    print_sudoku(S)
