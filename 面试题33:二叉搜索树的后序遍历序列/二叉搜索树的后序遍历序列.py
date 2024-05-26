#https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
'''
解题思路：
后序遍历得到的序列中，最后一个数字是根节点的值。除去根节点的值，数组中的其他值可以分为两个部分，一个是左子树的值，都小于根节点；一个是右子树的值，都大于根节点。

整体的思路就是根据根节点去寻找左子树的范围，然后去右子树中找有没有小于根节点的值，如果存在，必不是二叉搜索树。如果不存在，则将左右子树进行递归。
'''
class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        if not postorder:#空树符合二叉搜索树
            return True
        root=postorder[-1]#找到父节点
        index=0#初始化左子树的范围
        for node in postorder[:-1]:#在去除父、节点的序列中寻找左子树的范围，标准是小于父节点的值，如果出现大于根节点的值，证明已经到了右子树
            if node>root:
                break
            index+=1#索引加一
        for node in postorder[index:-1]:#对右子树进行遍历，如果发现有小于父节点的值，则这棵树肯定不是二叉搜索树
            if node<root:
                return  False
        left=True#先初始化左子树，防止左子树为空
        if index>0:#如果左子树不为空，判断左子树是否满足二叉搜索树的要求
            left=self.verifyTreeOrder(postorder[:index])
        right=True#先初始化右子树，防止右子树为空
        if index<len(postorder)-1:#如果右子树不为空，判断右子树是否满足二叉搜索树的要求
            right=self.verifyTreeOrder(postorder[index:-1])
        return left and right#判断左右子树是否都符合二叉树搜索树的条件
