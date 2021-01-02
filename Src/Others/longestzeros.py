
def solution(N):
    # write your code in Python 3.6
    s=bin(N)[2:]
    print(s)
    c=ret=0
    l,r=0,len(s)-1
    while l < r and s[l] != '1':
        l+=1
    while l < r and s[r] != '1':
        r-=1
    print(l,r)
    while l < r:
        while s[l]=='0':
            c+=1
            l+=1
        ret=max(ret,c)
        l+=1
        c=0
    return ret

print(solution(15))
print(solution(1041))
