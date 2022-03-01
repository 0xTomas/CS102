dna_1 = "ACTGTT"
dna_2 = "CCAGCA"


def longest_common_subsequence(string_1, string_2):
    print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))

    grid = [[0 for column in range(len(string_1) + 1)] for row in range(len(string_2) + 1)]

    result = ""
    for row in range(1, len(string_2) + 1):
        print("Comparing: {0}".format(string_2[row - 1]))
        for column in range(1, len(string_2) + 1):
            print("Against: {0}".format(string_1[column - 1]))
            if string_1[column - 1] == string_2[row - 1]:
                grid[row][column] = grid[row - 1][column - 1] + 1

            else:
                grid[row][column] = max(grid[row - 1][column], grid[row][column - 1])

        # Construct subsequence:
        result = []
    while row > 0 and column > 0:
        if string_1[column - 1] == string_2[row - 1]:
            result.append(string_1[column - 1])
            row -= 1
            column -= 1
        elif grid[row - 1][column] > grid[row][column - 1]:
            row -= 1
        else:
            column -= 1
        result.reverse()
        print("".join(result))

    for row_line in grid:
        print(row_line)


longest_common_subsequence(dna_1, dna_2)