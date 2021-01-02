'''
determine if chracters in a string is unique
'''

# O(n) time
# O(1) space since d can never has more than ascii_letters length.
def is_unique(s):
    import collections
    d=collections.defaultdict(int)
    for c in s:
        d[c]+=1
        if d[c] > 1:
            return False
    return True

## to do: understand setbit and get bit
def is_unique2(s):
    checker=0
    for c in s:
        val=ord(c)-ord('a')
        print(val,1<<val,checker & (1 << val))
        if checker & (1 << val) > 0:
            return False
        checker |= (1 << val)
        print(checker)
    return True

print(is_unique2("zazbc"))
print(is_unique("abca"))
