#https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
'''
解题思路：对n进行遍历，每次计算n&(n-1)的值，也就是将n中的最低位的1变为0
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0#初始化结果
        while n:#对n进行遍历
            n=n&(n-1)#对n和n-1做与运算，目的是将n中最低位的1变为0
            res+=1#结果加一
        return res#返回结果
