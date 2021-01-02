''' given two strings, decide if one is a permuation of other'''

## O(len(s)) time
## O(len(s)) space
def check_permutation(s1,s2):
    import collections
    d=collections.defaultdict(int)
    if len(s1) != len(s2):
        return False

    for c in s1:
        d[c]+=1
    for c in s2:
        if c not in d:
            return False
        d[c]-=1
    for k in d.values():
        if k !=0:
            return False
    return True

print(check_permutation("abc","cba"))
