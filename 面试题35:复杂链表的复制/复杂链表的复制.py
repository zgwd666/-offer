#https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/
'''
解题思路：
哈希表法：

利用哈希表的查询特点，考虑构建原链表节点和新链表对应节点的键值对映射关系，再遍历构建新链表各节点的next和random引用指向即可。

算法流程：

1.若头节点head为空节点，直接返回null

2.初始化：哈希表hmap，节点cur指向头节点

3.复制链表

- 建立新节点，并向hmap添加键值对（原cur节点，新cur节点）
- cur遍历至原链表下一节点

4.构建新链表的引用指向

- 构建新节点的next和random引用指向
- cur遍历至原链表下一节点

5.返回值：新链表的头节点hmap[cur]
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return #若头节点head为空节点，直接返回null
        hmap={}#初始化哈希表
        cur=head#创建一个节点等于头节点
        while cur:#对cur进行遍历
            hmap[cur]=Node(cur.val)#键值对为cur 和cur值创建的节点
            cur=cur.next#移向下一个
        cur=head#cur指向head
        while cur: #对cur进行遍历
            hmap[cur].next=hmap.get(cur.next)#创建next指针
            hmap[cur].random=hmap.get(cur.random)#创建random指针
            cur=cur.next#移向下一个
        return hmap[head]#返回头节点
