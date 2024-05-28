#https://leetcode.cn/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
'''
解题思路：
采用动态规划的思路

1.确定dp数组以及下标的含义

dp[i]:第i天的最大利润为dp[i]

2.确定递推公式

dp[i]=max(dp[i-1]+sales[i],sales[i])

3.初始化

dp[0]=scale[0]

4.确定遍历顺序

从前向后遍历

5.举例推导dp数组
'''
class Solution:
    def maxSales(self, sales: List[int]) -> int:
        if len(sales)==1:#判断特殊情况
            return sales[0]
        dp=[0]*len(sales)#创建dp数组
        dp[0]=sales[0]#dp数组初始化
        for i in range(1,len(sales)):#进行遍历
            dp[i]=max(dp[i-1]+sales[i],sales[i])#根据递推公式计算
        return max(dp)#返回最大值
