'''
check if s is a permutation of a parlindrome

note: s.lower() return a new string
'''

def check_parlindrome_permutation(s):
    from collections import Counter
    s1=s.lower()
    d=Counter(s1).items()
    c=0
    for k,v in d:
        if k!=' ':
            if v%2!=0:
                c+=1
        if c>1: return False
    return True

print(check_parlindrome_permutation("Tact Coa"))
