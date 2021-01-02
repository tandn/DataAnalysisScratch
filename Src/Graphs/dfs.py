def subsets(nums):
    ret=[]
    partial=[]

    def dfs(i,partial,ret):
        if i==len(nums):
            ret.append(partial[:])
            return

        partial.append(nums[i])
        dfs(i+1,partial,ret)
        partial.remove(nums[i])
        dfs(i+1,partial,ret)


    dfs(0,partial,ret)
    return ret

print(subsets([1,2,3]))
