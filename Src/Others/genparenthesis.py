def genparentheses(n):
    ret=[]
    partial=""
    def dfs(i,j,partial):
        print("CALL",i,j,partial)
        if i==n and j==n:
            print("return inside",i,j,partial)
            ret.append("".join(partial))
            return
        if i < n:
            #print("before open",i,j,partial)
            partial += "("
            dfs(i+1,j,partial)
            #print("after open",i,j,partial)
            #partial.pop()
        if j < i:
            #print("before close",i,j,partial)
            partial += ")"
            dfs(i,j+1,partial)
            #partial.pop()
            #print("after close",i,j,partial)
        print("return outside",i,j,partial)

    dfs(0,0,partial)
    return ret

print(genparentheses(2))
