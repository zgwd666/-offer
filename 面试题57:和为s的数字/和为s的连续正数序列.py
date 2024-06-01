#https://leetcode.cn/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
'''
解题思路：
采用双指针的思路，使用两个指针l,r分别指向1，2，进行遍历当l>=r结束

遍历中不断计算当前的和，根据当前的和分为三种情况

当前的和等于target，将当前的元素加入结果中，将l+1

当前的和小于target，将r+1

当前的和大于target，将l+1
'''
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        if target==1:#判断特殊情况
            return
        res=[]#初始化res
        l,r=1,2#初始化l,r
        stack=[l,r]#初始化stack
        while l<r:#进行遍历
            sumCur=(l+r)*(r-l+1)/2#计算当前的和
            if sumCur==target:#当前的和等于target，将当前的元素加入结果中，将l+1
                res.append(stack[:])
            if sumCur>=target:#当前的和大于target，将l+1
                l+=1
                stack.pop(0)
            else:#当前的和小于target，将r+1
                r+=1
                stack.append(r)
        return res#返回结果
