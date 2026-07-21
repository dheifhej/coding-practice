# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 链表删除的两种方式
# 直接使用原来的链表来进行删除操作。
# 设置一个虚拟头结点在进行删除操作。
# 通常不用管被删除节点的 next，只需要改前一个节点的指针就行
# 为什么会出现第二种，是不是发现，在单链表中移除头结点 和 移除其他节点的操作方式是不一样
# 可不可以 以一种统一的逻辑来移除 链表的节点 -
# 其实可以设置一个虚拟头结点，这样原链表的所有节点就都可以按照统一的方式进行移除了
# Optional[X] = 要么是 X，要么是 None
from typing import Optional

# 不特殊处理头节点的话，用一个dummyHead，即给原节点加个假头
class Solution:
    # Solution没写构造函数，但 Python 会自动给了一个默认构造函数
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next

        # 这样写的问题是追踪不到上个节点
        # currentNode = head
        # while currentNode is not None:
        #     if currentNode. == val:

        currentNode = head
        previousNode = None
        # 这段有问题，假设if成立，previousNode = currentNode挪到了被删除的节点上
        # while currentNode is not None:
        #     if currentNode.val == val:
        #         previousNode.next = currentNode.next
        #     previousNode = currentNode
        #     currentNode = currentNode.next
        while currentNode is not None:
            if currentNode.val == val:
                previousNode.next = currentNode.next    # 如果要删除头节点的特殊处理，previousNode.next就会报错，删除的前提是previousNode必须是个真的节点
                currentNode = currentNode.next
            else:
                previousNode = currentNode
                currentNode = currentNode.next

        return head

    def removeElements_m2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyNode = ListNode(next=head)
        currentNode = dummyNode
        while currentNode.next: # 相当于while current.next is not None
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next

        return dummyNode.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)

# 另一种构造链表的写法：用数组构造链表
def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next
list_2 = build_list([1, 2, 6, 3])

def print_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
print_list(head)

# 调用Solution前要先instantiate
solution = Solution()# Python 自动帮你做了内存分配（new）这一步

head = solution.removeElements(head, 6)
print_list(head)

# ❗️注意接住返回值，否则如果你删的头节点它还是会打印原列表，因为GC 只会回收“没有任何引用”的对象，你原来的 head 还有引用，所以不会被回收
# solution.removeElements(head, 1)
head = solution.removeElements(head, 1)
print_list(head)

