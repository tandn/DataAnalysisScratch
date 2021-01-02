'''
minimum size subarray sum
nums contains n positive integers
[2,3,1,2,4,3]
s=0,e=0

move e until cur >=s
s=0, e= 3, cur = 8,
            ret=4, cur=6,s=1
s=1, e=4, cur=10,
                ret=4,cur=7,s=2
                ret
s=2,e=5,cur

'''
import unittest
def minSubArrayLen(s,nums):
    i,n=0,len(nums)
    ret=n+1
    for j in range(n):
        s-=nums[j]
        while (s <= 0):
            ret=min(ret,j-i+1)
            s+=nums[i]
            i+=1
    return ret % (n+1)

class Test(unittest.TestCase):
    testcases=[(7,[2,3,1,2,4,3],2),
    ]

    funs=[minSubArrayLen]

    def test(self):
        for (s,nums,r) in self.testcases:
            for f in self.funs:
                print f(s,nums)

if __name__ == '__main__':
    unittest.main()

s = 7
nums = [2,3,1,2,4,3]
