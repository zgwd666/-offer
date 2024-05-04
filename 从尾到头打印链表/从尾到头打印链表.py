#https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
'''
解题思路：采用栈的方式，遍历链表，然后将链表的元素反转输出
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        if not head:#判断特殊情况
            return []
        stack=[]#初始化栈
        while head:#遍历链表
            val=head.val#提取节点值
            stack.append(val)#入栈
            head=head.next#移动到下一个节点
        return stack[::-1]#反转结果输出
