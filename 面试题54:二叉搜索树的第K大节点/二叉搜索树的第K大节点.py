#https://leetcode.cn/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
'''
解题思路：
二叉搜索树的特点是左子节点小于父节点小于右节点，我们可以采用中序遍历的方法，按照左中右的顺序，得到的结果是递增的结果，然后直接从后向前走cnt个找到答案
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        temp=[]#用来记录中序遍历结果
        def Inorder(root):
            if not root:#如果当前节点为空，直接返回
                return
            Inorder(root.left)#先遍历左节点
            temp.append(root.val)#记录当前节点值
            Inorder(root.right)#再遍历右节点
        Inorder(root)#进行中序遍历
        return temp[len(temp)-cnt]#从后向前数cnt个就行
