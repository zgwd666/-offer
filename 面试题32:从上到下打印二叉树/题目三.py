#https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
'''
解题思路：
本题在第二题的基础上加上一个指示单双行的信号即可，本质上仍然是对二叉树的广度优先遍历。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root::#空二叉树，返回空列表
            return []
        queue=[root]#二叉树根节点入队
        res=[]#创建一个空的结果列表
        flag=0#创建信号
        while queue:#对二叉树进行遍历
            level=[]#创建本层的结果列表
            for i in range(len(queue)):#对当前队中的每个节点进行遍历
                cur=queue.pop(0)#队头出队
                level.append(cur.val)#将当前元素的值加入到结果中
                if cur.left:#将当前元素的值加入到结果中
                    queue.append(cur.left)#左子节点入队
                if cur.right:#如果当前节点存在右子结点
                    queue.append(cur.right)#右子节点入队
            if flag==1:#如果现在是奇数行，则需要反转之后加入结果，并转换信号为0
                res.append(level[::-1])
                flag=0
            else:#如果当前是偶数行，直接加入结果，并转换信号为1
                res.append(level)
                flag=1
        return res #返回结果
