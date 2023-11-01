def print_matrix(matrix):
    for row in matrix:
        print(" ".join([f"{value:.6f}" for value in row]))

def calculate_c(k, m, z):
    n = k ** m
    c = [[0] * (z + 1) for _ in range(m + 1)]

    # Initialize the first row with all zeros
    for j in range(z + 1):
        c[0][j] = 0

    # Initialize the second row with 1/k
    for j in range(1, k + 1):
        c[1][j] = 1 / k
    print_matrix(c)
    for i in range(2, m + 1):
        for j in range(1, z + 1):
            if i > j or k * i > j:
                c[i][j] = 0
            else:
                for p in range(1, j):
                    c[i][j] += c[i - 1][p]
                c[i][j] *= 1.0 / k

    return c

# Input values
k = 6
m = 3
z = 10

# Calculate the c matrix
c = calculate_c(k, m, z)

# Print the c matrix
#print_matrix(c)
