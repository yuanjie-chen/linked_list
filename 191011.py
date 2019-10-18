import copy
class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

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

class Solution:
    def mergeTwoLinkedList(self, l1, l2):

        out = []
        current1 = l1
        current2 = l2
        if l1.value <= l2.value:
            current = l1
            first = current
            current1 = current1.next
            out.append(current.value)
        else:
            current = l2
            first = current
            current2 = current2.next
            out.append(current.value)
        while current1 and current2:

            if current1.value <= current2.value:
                current.next = current1
                current1 = current1.next
                current = current.next
                out.append(current.value)
            else:
                current.next = current2
                current2 = current2.next
                current = current.next
                out.append(current.value)

        if current1:
            current.next = current1
        elif current2:
            current.next = current2

        print(out)
        return first

    def sort_list(self, l1):
        sorted = []
        x = l1.pop(0)
        sorted.append(x)
        for element in l1:
            for i in range(len(sorted)):
                if i == 0 and sorted[i] > element:
                    sorted.insert(0,element)
                    break
                elif i== len(sorted) - 1 and sorted[i] < element:
                    sorted.insert(len(sorted),element)
                    break
                elif sorted[i] < element and sorted[i+1] >= element:
                    sorted.insert(i+1,element)
                    break
        return sorted



    def merge_lists(self,l1,l2):
        sorted_l1 = self.sort_list(l1)
        sorted_l2 = self.sort_list(l2)
        merged = []
        while len(sorted_l1) > 0 and len(sorted_l2) > 0:
            head1 = sorted_l1[0]
            head2 = sorted_l2[0]
            if head1 < head2:
                merged.append(head1)
                sorted_l1.pop(0)
            else:
                merged.append(head2)
                sorted_l2.pop(0)
        if len(sorted_l1) > 0:
            merged += sorted_l1
        elif len(sorted_l2) > 0:
            merged += sorted_l2
        return merged


    def roman_integer(self, input):
        number = 0
        if 'IV' in input:
            number += 4
            input = input.replace('IV', '')
        if 'IX' in input:
            number += 9
            input = input.replace('IX','')
        if 'XL' in input:
            number += 40
            input = input.replace('XL','')
        if 'XC' in input:
            number += 90
            input = input.replace('XC','')
        if 'CD' in input:
            number += 400
            input = input.replace('CD','')
        if 'CM' in input:
            number += 900
            input = input.replace('CM','')

        number += input.count('I') + input.count('V') * 5 + input.count('X') * 10 + input.count('L') * 50 + input.count('C') * 100 + input.count('D') * 500 + input.count('M') * 1000
        return number


s = Solution()
#s.mergeTwoList(a1,b1)
j = s.sort_list([1,4,6,8,2,6,3,8,4,23,495,38,7])
print(j)

k = s.merge_lists([4,6,7,66,4,6],[3,5,45,7,2,5])
print(k)
p = s.roman_integer('MCMXCIV')
print(p)

merged = s.mergeTwoLinkedList(a1,b1)
while merged.next:
    print(merged.value)
    merged = merged.next
print(merged.value)