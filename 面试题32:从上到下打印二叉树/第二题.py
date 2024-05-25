#https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
'''
解题思路：和题目一一样，对二叉树进行一个广度优先遍历，在遍历每行的时候定义一个数组存储本行的节点值即可。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:#空二叉树，返回空列表
            return []
        queue=[root]#二叉树根节点入队
        res=[]#创建一个空的结果列表
        while queue:#对二叉树进行遍历
            level=[]#创建本层的结果列表
            for i in range(len(queue)):#对当前队中的每个节点进行遍历
                cur=queue.pop(0)#队头出队
                level.append(cur.val)#将当前元素的值加入到本层结果中
                if cur.left:#将当前元素的值加入到结果中
                    queue.append(cur.left)#左子节点入队
                if cur.right:#如果当前节点存在右子结点
                    queue.append(cur.right)#右子节点入队
            res.append(level)#本层结果加入到总结果中
        return res#返回结果
