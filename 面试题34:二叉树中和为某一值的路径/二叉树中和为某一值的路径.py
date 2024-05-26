#https://leetcode.cn/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
'''
解题思路：
本题是典型的二叉树方案搜索问题，使用回溯法解决，其中包含了先序遍历和路径记录两个部分。

- 先序遍历：按照中左右的顺序下，遍历树的所有节点
- 路径记录：在先序遍历中，记录从根节点到当前节点的路径。当路径满足（1）根节点到叶结点所形成的路径（2）各节点值的和等于目标值target时，将此路径加入到结果列表中。

算法流程：

pathTarget(root,target)函数：

初始化：结果列表res，路径列表path

返回值：返回res即可

recur(root,tar)函数:

递推参数：当前节点root，当前目标tar

终止条件：若节点root为空，则直接返回。

递推工作：

- 路径更新，将当前节点值root.val加入到路径path
- 目标值更新：tar=tar-root.val（即目标值 `tar` 从 `target` 减至 000 ）
- 路径记录：当root为叶结点且路径和等于目标值，则将此路径path加入res
- 先序遍历：递归左右子结点
- 路径恢复：向上回溯时，需要将当前节点从路径path中删除，即执行path.pop()
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathTarget(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        res,path=[],[]#初始化结果和路径
        def recur(root,tar):#回溯算法
            if not root:#当前节点为空，返回
                return []
            tar-=root.val#计算还差多少
            path.append(root.val)#将当前节点加入路径
            if tar==0 and not root.left and not root.right:#root为叶结点且路径和等于目标值，则将此路径path加入res
                res.append(path[:])
            #递归左右子树
            recur(root.left,tar)
            recur(root.right,tar)
            #向上回溯时，需要将当前节点从路径path中删除，即执行path.pop()
            path.pop()
        recur(root,target)#进行递归
        return res#返回结果
