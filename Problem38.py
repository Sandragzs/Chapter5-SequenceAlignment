# 1. Defining the functions

def matrix_zeros(n,m):
    # Needed to solve the problem and keep the algorithm simple
    dp = [] # Empty list

    # Fill the list with zeros in the final structure
    i = 0 
    while i <= n: # i is the number of rows
        row = []
        j = 0

        while j <= m: # j is the number of columns
            row.append(0)
            j += 1
        # We add the row with j columns to dp
        dp.append(row)
        i += 1
    return dp


def lenght_longest_path(n, m, down, right):

    dp = matrix_zeros(n,m)

    # Fill the 1st row
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + right[0][j-1]

    # Fill the 1st column
    for i in range(1,n+1):
        dp[i][0] = dp[i-1][0] + down[i-1][0]

    # Fill the whole matrix
    for i in range(1, n+1):

        for j in range(1, m+1):

            value_1 = dp[i-1][j] + down[i-1][j]
            value_2 = dp[i][j-1] + right[i][j-1]

            dp[i][j] = max(value_1, value_2)

    return dp[n][m]



# Data:
n = 10
m = 19
down = [
    [1,4,0,2,3,2,2,3,0,3,2,0,1,4,1,1,4,4,3,4],
    [0,4,0,2,0,1,0,2,2,1,1,0,4,0,4,0,1,0,4,3],
    [0,1,4,3,3,0,1,1,1,0,2,2,1,2,2,1,4,4,3,4],
    [3,1,3,1,1,1,3,0,2,3,1,0,2,4,2,1,4,3,3,4],
    [3,2,1,2,2,2,3,3,4,3,3,1,2,4,1,1,4,2,3,1],
    [3,2,4,4,3,0,4,0,1,1,0,3,3,0,1,2,3,3,4,2],
    [1,3,0,4,2,1,1,4,0,0,0,3,2,1,2,3,4,4,0,3],
    [4,4,3,2,3,2,1,0,1,4,2,2,2,4,1,4,1,4,1,1],
    [0,1,1,2,1,1,2,1,2,4,4,0,0,2,4,2,4,1,4,0],
    [2,0,3,2,3,0,0,3,4,0,3,0,0,4,3,2,0,4,4,2]
]

right = [
    [2,4,3,0,0,3,2,3,3,4,4,0,1,2,0,0,0,4,2],
    [3,3,1,0,4,1,0,1,3,2,4,4,0,2,4,0,0,1,3],
    [3,2,2,0,2,0,1,4,1,4,4,0,1,0,2,2,2,0,2],
    [4,3,4,4,1,0,0,0,1,4,3,3,4,4,0,1,3,1,0],
    [0,4,1,1,0,4,4,4,4,0,0,2,0,2,4,0,3,3,4],
    [3,4,3,1,4,2,3,1,4,4,1,2,4,1,4,2,4,2,3],
    [0,4,3,2,4,2,4,2,1,4,4,0,4,2,4,1,3,2,3],
    [4,1,0,1,2,1,3,4,1,1,0,3,2,3,1,4,3,0,1],
    [2,2,0,2,0,0,4,2,0,1,4,0,1,1,2,4,2,0,2],
    [0,4,1,2,4,4,2,3,0,2,2,1,1,0,1,1,1,0,1],
    [1,0,4,4,0,1,4,0,1,1,4,4,2,1,0,3,2,3,4]
]


# 3. Printing the results
answer = lenght_longest_path(n, m, down, right)
print(answer)
        


