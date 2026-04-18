# 在链表类中实现这些功能：
#
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。

# Singly Linked List：在单链表中，每个节点只知道它的下一个节点是谁。
# Doubly Linked List：在双链表中，每个节点既知道它的下一个节点，也知道它的前一个节点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
        return current.val
    def addAtHead(self, value:int) -> None:
        self.dummy_head.next = ListNode(value, self.dummy_head.next)
        self.size += 1
    def addAtTail(self, value: int) -> None:
        current = self.dummy_head.next
        for i in range(self.size):  # while current.next:
            current = current.next
        current.next = ListNode(value)
        self.size += 1
    def addAtIndex(self, index: int, value:int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.dummy_head
        for i in range(index):
            prev = prev.next
        prev.next = ListNode(value, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.dummy_head
        for i in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1


def buildLinkedList(arr):
    list_node = ListNode()
    current = list_node
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return list_node.next

def printLinkedList(head):
    cur = head
    while cur:
        print(cur.val, end= "-> ")
        cur = cur.next
    print("None")

list_2 = buildLinkedList([1, 2, 6, 3])
printLinkedList(list_2)
# print(SinglyLinkedList.get(list_2, 0))
# 为什么你的 get 调用会失败？
# 你写的是：SinglyLinkedList.get(list_2, 0)。
# 这里有两个根本性的误区：get 是一个实例方法（第一个参数是 self）。你不能直接用类名去调用它并传一个 ListNode 进去。
# 错误写法：把 SinglyLinkedList 当成一个工具箱，把 list_2 丢进去处理。
# 正确逻辑：你应该先创建一个 SinglyLinkedList 的对象，然后在这个对象上操作。
# list_2 是通过 buildLinkedList 函数造出来的，它只是一串互相连接的 ListNode。
# 而 SinglyLinkedList 类是一个管理器，它内部包含 dummy_head 和 size。

# 1. 创建管理器对象
my_manager = SinglyLinkedList()

# 2. 通过管理器的 API 添加数据
my_manager.addAtHead(3)
my_manager.addAtHead(6)
my_manager.addAtHead(2)
my_manager.addAtHead(1) # 现在的逻辑相当于 [1, 2, 6, 3]

# 3. 让管理器去 get
print(my_manager.get(0)) # 输出 1
my_manager.deleteAtIndex(1)
print(my_manager.get(1))