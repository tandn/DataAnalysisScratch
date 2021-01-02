## maximum sum
def maximum_sum_subarray(arr):
    cur=ret=0
    for n in arr:
        if cur < 0:
            cur=0
        cur+=n
        ret=max(ret,cur)
    return ret

## maximum product
def maximum_product_subarray(arr):
    n=len(arr)
    if not arr or n==0:
        raise Exception("arr is empty")
    postfix=arr[::-1]
    for i in range(1,n):
        arr[i]*=(arr[i-1] or 1)
        postfix[i]*=(postfix[i-1] or 1)
    return max(arr + postfix)


a=[]
print(maximum_sum_subarray(a))
print(maximum_product_subarray(a))
