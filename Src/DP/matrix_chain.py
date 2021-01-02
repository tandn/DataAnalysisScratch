# Matrix multiplication
# n matrix A1,A2,.. => n+1 dimension vector
# ex: p = [10 100 5 50] => represent three matricies 10 x 100, 100 x 5, 5 x 50
# output minimum cost of matrix chain multiplication

def matrix_chain(p):
    n=len(p)
    #dp[i][j]: optimal cost of multiplying Ai .. Aj
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(2,n):
        for i in range(n):
            for j in range(i+1,n):
                dp[i][j]=float('inf')
            # guess the last position of multiplication k
                dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j] + p[i]*p[k]*p[j])
    print(n,dp)
    return dp[n-1][n-1]


p=[0,100,5,50]
print(matrix_chain(p))
