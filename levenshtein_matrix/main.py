def levenshtein_matrix(string1: str, string2: str, print_matrix: bool = False) -> int:

    # Create a matrix of the indices 
    n, m = len(string1), len(string2)
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        matrix[i][0] = i
    for j in range(m+1):
        matrix[0][j] = j
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if string1[i - 1] == string2[j - 1]:
                sub_cost = 0
            else:
                sub_cost = 1
            
            matrix[i][j] = min(
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + sub_cost
            )
    if print_matrix:
        for line in matrix:
            print(f"{line}\n")
    
    return matrix[n][m]


def main():
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    print("The edit distance of string", string1, "and string", string2, "is", levenshtein_matrix(string1, string2))

if __name__ == "__main__":
    main()

