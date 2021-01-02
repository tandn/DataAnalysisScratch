'''
compress a string
O(n)
'''
def compress(s):
    i,ret=0,""
    while i < len(s):
        l=1
        c=s[i]
        while i+1 < len(s) and c==s[i+1]:
            i+=1
            l+=1
        ret+=c+str(l)
        i+=1

    if len(ret) > len(s):
        return s
    else:
        return ret

print(compress("aabccccaaa"))
