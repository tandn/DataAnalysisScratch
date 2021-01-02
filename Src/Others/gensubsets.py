def gensubsets(nums):
    partial=[]
    ret=[]
    def dfs(i,partial):
        if i == len(nums):
            ret.append(partial)
            return
        partial.append(nums[i])
        dfs(i+1,partial)
        partial.pop()
        dfs(i+1,partial)

    dfs(0,partial)
    return ret

print(gensubsets([1,2,3]))
