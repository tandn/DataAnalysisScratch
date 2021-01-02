'''
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.'''
import unittest
def consecutive_ones(arr):
    if not arr or len(arr)==0:
        return 0
    c=0
    ret=1
    f=False
    for i,n in enumerate(arr):
        if n:
            c+=1
        elif not f:
            c+=1
            f=True
        else:
            c=0
        ret=max(ret,c)
    return max(ret,c)


class Test(unittest.TestCase):
    testcases = [
        ([1,0,1,1,0],4),
        ([0,0,0,0,0],1),
        ([],0),
        ([0],1),
        ([1,1,1,1,1,0,1,1,1,1],10),
    ]
    def test_consecutive_ones(self):
        for (arr,ret) in self.testcases:
            assert consecutive_ones(arr) == ret

if __name__ == '__main__':
    unittest.main()
