#https://leetcode.cn/problems/zhong-jian-er-cha-shu-lcof/
'''
解题思路：前序遍历的第一个数字就是根节点的值，然后通过根节点的值去中序遍历的结果中查找index，index之前的是左子树，index之后的是右子树；然后根据index去前序遍历的查找，1-index+1是左子树；index+1之后的是右子树。然后不断递归得到结果。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deduceTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:#如果前序数组为空，证明已经递归结束
            return 
        #找到根节点
        val=preorder[0]
        root=TreeNode(val)
        #根据根节点在中序遍历的结果中找到左子树和右子树的分割点
        index=inorder.index(val)
        #分隔左子树和右子树
        leftInorder=inorder[:index]
        rightInorder=inorder[index+1:]
        leftPreorder=preorder[1:index+1]
        rightPreorder=preorder[index+1:]
        #计算左子树和右子树
        root.left=self.deduceTree(leftPreorder,leftInorder)
        root.right=self.deduceTree(rightPreorder,rightInorder)
        return root
