#https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/
'''
解题思路：
对二叉树进行层序遍历，每遍历一层加一，计算最终的结果即可。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0#如果为空树，则直接返回0
        queue=[root]#将根节点加入队列中
        res=0#初始化结果
        while queue:#对队列进行遍历
            for _ in range(len(queue)):#遍历本层的所有节点
                cur=queue.pop(0)#从队列的左边弹出
                if cur.left:#存在左子节点将左子节点加入队列
                    queue.append(cur.left)
                if cur.right:#存在右子节点将右子节点加入队列
                    queue.append(cur.right)
            res+=1#本层节点遍历完成，结果加一
        return res#返回结果
