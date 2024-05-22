#https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
'''
解题思路：
需要创建两个节点，一个节点指向head，另一个节点等于head

然后遍历head，统计节点的个数。

如果节点的数量小于cnt，返回-1

否则的话倒数第cnt个节点也就是正数count-cnt个节点
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        cur=ListNode(-1)#创建一个伪节点
        cur.next=head#伪节点指向head
        dumn=cur.next#创建另一个伪节点等于head
        count=0#初始化count
        while head:#遍历链表，统计数量
            count+=1
            head=head.next
        if count<cnt:#如果节点的数量小于cnt，返回-1
            return -1
        for i in range(count-cnt):#否则的话倒数第cnt个节点也就是正数count-cnt个节点，进行遍历
            dumn=dumn.next
        return dumn#返回结果
