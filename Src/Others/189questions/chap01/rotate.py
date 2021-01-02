''' Rotate closewise
 m=[[1,2,3],
    [4,5,6],
    [7,8,9]]
 rotate m 90 degree
 output: first row = last column, second row = second last collum,..
  [[7,4,1],
  [8,5,2],
  [9,6,3]]

b[i,j]=a[j,i] = first row= first collum, second row= second collum
b[1,:]=a[:,1]
  [1,4,7], r=0, c=1,2 [0][1] <-> [1][0], [0],[2]
  [2,5,8], r=1, c=0,2
  [3,6,9]  r=2
'''
def rotate(m):
    row=len(m)
    col=len(m[0])
    for r in range(row):
        for c in range(r+1,col):
            m[r][c],m[c][r]=m[c][r],m[r][c]
    for c in range(col//2):
        for r in range(row):
            m[r][c],m[r][col-c-1]=m[r][col-c-1],m[r][c]


m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
rotate(m)
print(m)
