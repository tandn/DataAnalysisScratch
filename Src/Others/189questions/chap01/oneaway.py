'''
determine if a string can be converted to another in one step
using ordereddict to store the difference between s1,s2
tolerate up to 2 characters difference
'''
def one_away(s1,s2):
    from collections import OrderedDict
    d=OrderedDict()
    n1,n2=len(s1),len(s2)
    if abs(n1-n2) > 1:
        return False
    for c in s1:
        d[c]=d.get(c,0) + 1
    for c in s2:
        d[c]=d.get(c,0) - 1

    c=0
    for k,v in d.items():
        c+=abs(v)
        if c > 2:
            return False
    return True

print(one_away("pale","agle"))
