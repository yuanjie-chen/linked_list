def test_1_1():
    assert 1 == 1

#tests for the class Solution
from linked_list191011 import *
a1 = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(20)
a1.next = a2
a2.next = a3
b1 = ListNode(3)
b2 = ListNode(5)
b3 = ListNode(19)
b1.next = b2
b2.next = b3

def test_define_merged_linked_lists():
    s = Solution()
    a1 = ListNode(2)
    a2 = ListNode(4)
    a3 = ListNode(20)
    a1.next = a2
    a2.next = a3
    b1 = ListNode(3)
    b2 = ListNode(5)
    b3 = ListNode(19)
    b1.next = b2
    b2.next = b3
    output = s.mergeTwoLinkedList(a1, b1)
    assert output.value == 2
    #assert output.next.next.value == 4
    #assert output.next.next.next == 5


#pytest.assume