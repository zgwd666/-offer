#https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
'''
解题思路 ：
采用递归的解法，输入的参数为A和B两棵树，停止条件为两棵树任意一颗树节点为空，返回。递归中对当前节点的值以及当前节点的左右子树进行匹配判断
对于主函数而言，就是寻找大树的所有节点看看有没有能和小树匹配上的。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(A,B):#递归函数
            if not B:#当B的节点先为空，证明A包含B，返回True
                return True
            if not A :#当A的节点先为空，证明B不在A中，返回False
                return False
            return A.val==B.val and dfs(A.right,B.right) and dfs(A.left,B.left)#树匹配的条件是当前节点值相等以及左右子树相等
        if not A or not B:return False#当输入的树有一颗为空，返回False
        return dfs(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)#返回当前节点为B的根节点的匹配情况和以当前节点的左右子结点为B的根节点的匹配情况
