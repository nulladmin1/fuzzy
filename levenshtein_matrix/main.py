# Adapted from the wikipedia article from this topic:
# https://en.wikipedia.org/wiki/Levenshtein_distance


# Levenshtein Fuzzy Search algorithm - using matrices and dynamic programming
# This algorithm finds the edit distance between 2 strings
# The edit distance is the minimum amount of single-character edits required to change one word to another

# For a string1 kitten and string2 sitting:
#   1) kitten → sitten (substitution of "s" for "k")
#   2) sitten → sittin (substitution of "i" for "e")
#   3) sittin → sitting (insertion of "g" at the end)
# So then the edit distance will be 3

# This algorithm is definitely not the fastest one,
# But it does its job good enough for a simple fuzzy search algorithm
# It's complexity is:
#   Time: O(n*m)
#   Auxillary: O(n*m)

# Create function levenshtein_matrix() that takes in a string string1, a string string2, and optionally a print_matrix boolean for printing.
# It returns the edit distance as an integer
def levenshtein_matrix(string1: str, string2: str, print_matrix: bool = False) -> int:

    # Make variables n and m that store the length of both input strings
    n, m = len(string1), len(string2)

    # Initialize a matrix with zeroes
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # Fill the first column and first row with the base cases for edit distance - 
    #   the edit distance between the first i characters of string1 and an empty string2 requires i deletions
    #   the edit distance between the first j characters of string2 and an empty string1 requires j insertions
    for i in range(n+1):
        matrix[i][0] = i
    for j in range(m+1):
        matrix[0][j] = j
    
    # Use dynamic programming:
    # Iterate through the matrix
    for i in range(1, n+1):
        for j in range(1, m+1):
            if string1[i - 1] == string2[j - 1]: # Check if there is substitution - if no, then set it to zero
                sub_cost = 0
            else:
                sub_cost = 1                    # Else: set it to 1
            
            matrix[i][j] = min(                 # Get the minimum cost of:
                matrix[i-1][j] + 1,             #   1) Deletion
                matrix[i][j-1] + 1,             #   2) Insertion
                matrix[i-1][j-1] + sub_cost     #   3) Substitution
            )
    
    # Optionally print the matrix after done
    if print_matrix:
        for line in matrix:
            print(f"{line}\n")
    
    # The last value of the matrix ([n, m]) contains the final edit_distance
    return matrix[n][m]


def main():
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    print("The edit distance of string", string1, "and string", string2, "is", levenshtein_matrix(string1, string2))
    
if __name__ == "__main__":
    main()

