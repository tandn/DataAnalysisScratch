def pow(a,b):
    dp={}
    def go(a,b):
        if (a,b) in dp:
            return dp[(a,b)]
        if b==0:
            return 1
        if b%2 == 0:
            if (a,b//2) not in dp:
                dp[(a,b//2)] = go(a,b//2)
            dp[(a,b)] = dp[(a,b//2)] * dp[(a,b//2)]
            return dp[(a,b)]
        else:
            if (a,b//2) not in dp:
                dp[(a,b//2)] = go(a,b//2)
            dp[(a,b)] = dp[(a,b//2)] * dp[(a,b//2)] * a
            return dp[(a,b)]

    res=go(a,abs(b))*1.0
    return res if b > 0 else 1.0/res

print(pow(12,12))
