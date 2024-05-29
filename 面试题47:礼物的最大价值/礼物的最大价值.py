#https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/
'''
解题思路：
可以采用动态规划的思路来做

1.确定dp数组以及下标的含义

$$dp[i][j]：代表在(i,j)位置上能获取的珠宝的最大值$$

2.确定递推公式

因为只能从向右或者向下移动，所以

$$dp[i][j]=max(dp[i-1][j],dp[i][j-1])+frame[i][j]$$

3.初始化

$$首先是dp[0][0]就是左上角的珠宝的价值，所以dp[0][0]=frame[0][0]$$

$$对于第一列：dp[i][0]=dp[i-1][0]+frame[i][0]$$

$$对于第一行：dp[0][i]=dp[0][i-1]+frame[0][i]$$

4.确定遍历顺序

从上到下从左到右

5.举例推导dp数组
'''
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        if len(frame)==0:#判断特殊情况
            return 0
        dp=[[0 for i in range(len(frame[0]))]for i in range(len(frame))]#创建状态转移数组
        #初始化
        dp[0][0]=frame[0][0]
        for i in range(1,len(frame)):
            dp[i][0]=dp[i-1][0]+frame[i][0]
        for i in range(1,len(frame[0])):
            dp[0][i]=dp[0][i-1]+frame[0][i]
        #进行遍历
        for i in range(1,len(frame)):
            for j in range(1,len(frame[0])):
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])+frame[i][j]#按照递推公式计算当前的状态
        return dp[-1][-1]#返回最终结果
