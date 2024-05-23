#https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
'''
解题思路：
采用伪节点循环的方式，定义一个伪节点，定义一个临时节点等于伪节点，伪节点的作用是用来定位。

对l1和l2进行遍历，当l1的值更小，则临时节点指向l1当前节点，l1向后移动，否则当前节点指向l2当前节点，l2向后移动。不管指向哪个节点，当前节点指向结束之后需要移动

最后返回伪节点的下一位即可
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainningPlan(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:#l1不存在，直接返回l2
            return l2
        if not l2:#l2不存在，直接返回l1
            return l1
        dumn=ListNode(-1)#创建伪节点
        cur=dumn#创建临时节点
        while l1 and l2:#遍历l1和l2
            if l1.val<l2.val:#当l1的值小
                cur.next=l1#临时节点指向l1
                l1=l1.next#l1向后移动
            else:#否则
                cur.next=l2#临时节点指向l2
                l2=l2.next#l2向后移动
            cur=cur.next#临时节点向后移动
        if l1:#如果l1还有剩余，则将剩余的都加进来
            cur.next=l1
        if l2:#如果l1还有剩余，则将剩余的都加进来
            cur.next=l2
        return dumn.next#返回伪节点的next作为结果
