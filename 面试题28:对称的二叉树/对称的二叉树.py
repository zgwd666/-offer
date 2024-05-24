#https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/
'''
解题思路：
对称二叉树的定义：对于树中任意两个对称节点L和R，一定存在如下特性：

L.val=R.val:两个对称节点的值相等

L.right.val=R.left.val:即L的右子节点和R的左子节点对称

L.left.val=R.right.val:即L的左子节点和R的右子节点对称

根据如上的特性，考虑从顶至底递归，判断每对左右节点是否对称，从而判断树是否为对称二叉树
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetricTree(self, root: Optional[TreeNode]) -> bool:
        if not root:#如果为空树，也是对称的
            return True
        def recur(L,R):#定义一个递归函数，用于判断是否为对称
            if not L and not R:return True#当左子树和右子树同时为空，True
            if not L or not R:return False#当仅有一棵树为空，Fasle
            return L.val==R.val and recur(L.left,R.right) and recur(L.right,R.left)#根据对称二叉树的特性进行判断
        return recur(root.left,root.right)#返回判断结果
