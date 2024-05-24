#https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/
'''
解题思路：采用递归的解法，考虑递归遍历二叉树，交换每个节点的左右子节点，即可生成二叉树的镜像。

1.终止条件：当节点root为空时（即越过叶结点），则返回None

2.递推流程：先交换当前节点的左右子节点，然后递归交换后的左右子节点

3.返回值：返回当前节点root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:#当前节点为空，返回None
            return None
        root.left,root.right=root.right,root.left#先交换当前节点的左右子节点
        self.mirrorTree(root.left)#对交换后的左子树进行递归
        self.mirrorTree(root.right)#对交换后的右子树进行递归
        return root#返回根节点
