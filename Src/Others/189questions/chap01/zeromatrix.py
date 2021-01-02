def zero(m):
    row=len(m)
    col=len(m[0])
    zeros=[-1]*row
    for i in range(row):
        for j in range(col):
            if i < row and m[i][j]==0:
                zeros[i]=j
                i+=1
    print(zeros)

m=[[0,1,2],
    [3,0,5],
    [6,7,8]]
zero(m)
