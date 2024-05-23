#https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/
'''
解题思路：
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:#如果空链表直接返回
            return head
        pre=None#创建一个为空的节点
        while head:#对head进行遍历
            temp=head.next#将当前节点的下一个节点进行存储
            head.next=pre#当前节点的下一个节点指向pre
            pre=head#pre等于当前节点
            head=temp#节点向后移动
        return pre#返回反转后的链表
