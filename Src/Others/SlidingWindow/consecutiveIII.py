import unittest
def consecutive_onesIII(arr,k):
    if not arr or len(arr)==0:
        return 0
    c=0
    ret=0
    t=k
    for i,n in enumerate(arr):
        if n:
            c+=1
        else:
            if t:
                c+=1
                t-=1
            else:
                t=k-1
                c=1
        ret=max(ret,c)
        print(n,t,c,ret)
    return max(ret,c)


class Test(unittest.TestCase):
    testcases = [
        ([1,0,1,1,0],1,4),
        ([0,0,0,0,0],1,1),
        ([],1,0),
        ([0],1,1),
        ([1,1,1,1,1,0,1,1,1,1],1,10),
        ([1,1,1,0,0,0,1,1,1,1,0],2,6),
    ]
    def test_consecutive_ones(self):
        for (arr,k,ret) in self.testcases:
            assert consecutive_onesIII(arr,k) == ret

if __name__ == '__main__':
    unittest.main()

print(consecutive_onesIII([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
