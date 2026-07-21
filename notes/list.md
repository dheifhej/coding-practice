# node = ListNode(5)
# 向操作系统要一块内存，操作系统在“当前空闲的内存里找一块能放下的地方”
# that can be previously freed memory/fragmented space/any available location
# Linked list nodes are scattered in memory and connected by pointers, not stored next to each other like arrays.
# Nodes are not stored contiguously

# // 单链表
# // 在 C++ 里，struct 也可以有构造函数，写构造函数是为了：创建节点时自动初始化
# struct ListNode {
#     int val;  // 节点上存储的元素
#     ListNode *next;  // 指向下一个节点的指针
#     ListNode(int x) : val(x), next(NULL) {}  // 节点的构造函数
# };
# // 如果不写构造函数会怎样，那就必须手动写：
# ListNode* node = new ListNode;
# node->val = 5;
# node->next = NULL;
# 链表删除节点 ≠ 内存释放，假设A→ B → C → D → E 删除了D，
# 在c++里要再手动释放这个D节点所在内存，其他语言如Java、Python，就有自己的内存回收机制（Garbage Collection + 引用计数），就不用自己手动释放了。
# 链表的增添和删除都是O(1)操作
# array 查询是O(1)，因为可以直接通过“下标公式”算出内存地址，毕竟是连续内存
# 所以得出array适合数据量固定，较少增删和频繁查询的数据
# 链表适合较多增删，数据量不固定，较少查询的数据
# class ListNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

# 在 __init__ 方法中，数字（或其他初始值）通常代表这个对象的**“出生状态”**。