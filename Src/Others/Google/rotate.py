'''
source: https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
m=[ [1,2,3],
    [4,5,6],
    [7,8,9]]
m.transpose
m=[ [1,4,7],
    [2,5,8 ]
    [3,6, 9]]
m.swap
m = [3,6,9]...
'''
def rotate(m): #anti closewise
    n=len(m)
    # transpose the matrix in place
    for i in range(n):
        for j in range(i+1,n):
            m[i][j],m[j][i]=m[j][i],m[i][j]
    ## swap row
    for i in range(n//2):
        for j in range(n):
            m[i][j],m[n-i-1][j]=m[n-i-1][j],m[i][j]

m=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(m)
print(m)
