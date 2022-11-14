class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def add_two_numbers(l1, l2):
#     temp = 0
#     sum1 = l1.val + l2.val
#     if sum1 > 9:
#         temp = sum1 // 10
#         sum1 = sum1 % 10
#     returning_list = ListNode(sum1)
#     while isinstance(l1.next, ListNode) and isinstance(l2.next, ListNode):
#         sum1 = l1.next.val + l2.next.val
#         if temp > 0:
#             sum1 += temp
#         if sum1 > 9:
#             temp = sum1 // 10
#             sum1 = sum1 % 10
#         returning_list.next = sum1
#         l1 = l1.next
#         l2 = l2.next
#     return returning_list


l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, 9)))))
l2 = ListNode(9, ListNode(9, ListNode(9, 9)))


# def addTwoNumbers(l1, l2):
#     temp = 0
#     sum1 = l1.val + l2.val
#     if sum1 > 9:
#         temp = sum1 // 10
#         sum1 = sum1 % 10
#     returning_list1 = ListNode(sum1)
#     returning_list2 = returning_list1
#     while (l1.next is not None) or (l2.next is not None):
#         if isinstance(l1.next, int) and isinstance(l2.next, int):
#             sum1 = (0 if l1.next is None else l1.next) + (0 if l2.next is None else l2.next)
#         else:
#             sum1 = (0 if not hasattr(l1.next, 'val') else l1.next.val) + (
#                 0 if not hasattr(l2.next, 'val') else l2.next.val)
#         if temp > 0:
#             sum1 += temp
#         if sum1 > 9:
#             temp = sum1 // 10
#             sum1 = sum1 % 10
#         if isinstance(l1.next, int) and isinstance(l2.next, int):
#             returning_list2.next = sum1
#         else:
#             returning_list2.next = ListNode(sum1)
#         if isinstance(l1.next, ListNode) or isinstance(l2.next, ListNode):
#             l1 = ListNode(0) if l1.next is None else l1.next
#             l2 = ListNode(0) if l2.next is None else l2.next
#             returning_list2 = returning_list2.next
#         else:
#             break
#     return returning_list1


def addTwoNumbers(l1, l2):
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0
    while l1 != None or l2 != None or carry != 0:
        l1Val = l1.val if hasattr(l1, 'val') else 0
        l2Val = l2.val if hasattr(l2, 'val') else 0
        columnSum = l1Val + l2Val + carry
        carry = columnSum // 10
        newNode = ListNode(columnSum % 10)
        curr.next = newNode
        curr = newNode
        l1 = l1.next if hasattr(l1, 'next') else None
        l2 = l2.next if hasattr(l2, 'next') else None
    return dummyHead.next


a = addTwoNumbers(l1, l2)
# print(a.val, a.next.val, a.next.next)
