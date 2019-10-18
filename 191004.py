import copy
class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None


#Homework
#add a node 100(after 13, at nth index)
#delete a node (delete 13, after nth index)

def createlinkedlist1():
    l1 = ListNode(2)
    l2 = ListNode(5)
    l3 = ListNode(6)
    l4 = ListNode(13)
    l5 = ListNode(5)
    l6 = ListNode(13)
    l7 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    return l1


def remove13(l1):
    output = []
    previous = None
    current = l1
    while current.next:
        #print(current.value)
        if current.next.value == 13:
            current.next = current.next.next
        previous = copy.deepcopy(current)
        current = current.next
    if current.value == 13:
        previous.next = None
    if l1.value == 13:
        l1 = l1.next

    current = l1
    while current.next:
        #print(current.value)
        output.append(current)
        current = current.next
    output.append(current)
    print([i.value for i in output])
    return output


#l1 = createlinkedlist1()

#out = remove13(l1)

def add100_after13(l1):
    output = []
    previous = None
    current = l1
    while current.next:
        print(current.value)
        if current.next.value == 13:
            inserted = ListNode(100)
            inserted.next = current.next.next
            current.next.next = inserted
        previous = copy.deepcopy(current)
        current = current.next
    if l1.value == 13:
        temp = ListNode(100)
        temp.next = l1.next
        l1 = temp
    current = l1

    while current.next:
        print(current.value)
        output.append(current)
        current = current.next
    output.append(current)
    print([i.value for i in output])
    return output

#out2 = add100_after13(l1)

def add_node(l1,n,listnode):
    output = []
    current = l1
    for i in range(n-1):
        if current.next:
            current = current.next
        else:
            print('index out of range')
            return
    listnode.next = current.next
    current.next = listnode
    current = l1
    while current.next:
        #print(current.value)
        output.append(current)
        current = current.next
    output.append(current)
    print([i.value for i in output])
    return output

#add_node(l1,30,ListNode(512))

#sort linked list

class Solution:
    def mergeTwoList(self, l1, l2):

        out = []
        current1 = l1
        current2 = l2
        if l1.value <= l2.value:
            current = l1
            current1 = current1.next
            out.append(current.value)
            first = l1
        else:
            current = l2
            current2 = current2.next
            out.append(current.value)
            first = l2
        while current1 and current2:

            if current1.value <= current2.value:
                current.next = current1
                current1 = current1.next
                out.append(current.value)
                current = current.next
            else:
                current.next = current2
                current2 = current2.next
                out.append(current.value)
                current = current.next

        if current1:
            current.next = current1
        elif current2:
            current.next = current2

        print(out)
        return first


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a4 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4


b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

s = Solution()
s.mergeTwoList(a1,b1)