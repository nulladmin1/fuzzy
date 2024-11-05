def levenshtein(string1: str, string2: str) -> int:

    # Create a matrix of the indices 
    n, m = len(string1), len(string2)
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    print(matrix)
    
    for x in range(0, n+1):
        matrix[x][0] = x
    for x in range(0, m+1):
        matrix[0][x] = x

    for l in matrix:
        print(f"{l}\n")
    
    for i in range(1, n+1):
        matrix[0][i] = i
        for j in range(1, m+1):
            if string1[i] == string2[j]:
                sub_cost = 0
            else:
                sub_cost = 1
            
            matrix[i][j] = min(
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + sub_cost,
            )
    for l in matrix:
        print(f"{l}\n")
    
    return matrix[n][m]


def main():
    print("Hello World!")
    print(levenshtein("kitten", "sitting"))

if __name__ == "__main__":
    main()

