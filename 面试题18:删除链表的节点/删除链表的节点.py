#https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/
'''
解题思路：采用一个伪节点来进行过渡，在遍历到要去除的节点的时候，使得head.next=head.next.next即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        cur=ListNode(-1)#创建一个伪节点
        if head.val==val:#当head的头节点为目标值的时候，将头节点的指针向后移动
            head=head.next
        cur.next=head#将伪节点指向头节点
        while head and head.next:#当头节点和头节点的下一个节点都存在的时候进行遍历
            if head.next.val==val:#如果下一个节点的值等于目标值
                head.next=head.next.next#使得当前节点的下一个节点等于下一个节点的下一个节点，也就是直接跳过下一个节点
            head=head.next#将当前节点向下一个节点移动
        return cur.next#返回头节点
