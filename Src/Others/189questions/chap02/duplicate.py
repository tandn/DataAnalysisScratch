import unittest
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def remove_dups(head):
    checker=0
    while head:
        print(head.val, checker)
        if checker & (1 << head.val) > 0:
            return False
        checker |= (1 << head.val)
        head=head.next
    return True

class Test(unittest.TestCase):
    test_cases = [
        (Node(1,Node(2,Node(2))), False),
        (Node(1,Node(1,Node())), True),
        (None, True),
        (Node(1,Node(2,Node(3))), False),
    ]

    def test_remove_dups(self):
        for (xs, expected) in self.test_cases:
            print(remove_dups(xs))
            #assert remove_dups(xs) == expected


if __name__ == "__main__":
    unittest.main()
