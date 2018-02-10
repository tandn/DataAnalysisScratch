from collections import Counter, defaultdict
import random

for i in [1, 2, 3, 4, 5]:
    print i # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print j # first line in "for j" block
        print i + j # last line in "for j" block
    print i # last line in "for i" block
print "done looping"


# string
b = ["s" + str(i) for i in range(100)] == ['s' + str(i) for i in range(100)]
print(b)

# lazy range

def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i = i + 1

# list comprehension

triangle =[(a,b,c)
           for a in range(1,10)
           for b in range(1,10)
           for c in range(1,10)
           if a*a + b*b == c*c]

print(triangle)

# random ness

uniform = [random.random() for _ in range(4)]
print(uniform)
