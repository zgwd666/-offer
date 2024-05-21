#https://leetcode.cn/problems/jian-sheng-zi-lcof/
'''
解题思路：
采用动态规划的思路

1.确定dp数组以及下标的含义

dp[i]:长度为i的竹子砍过之后所能组成的最大乘积

2.递推公式

dp[i]存在三种得到的途径。

1.不剪，则dp[i]=dp[i]

2.只剪一刀，那么dp[i]=j*(i-j) j代表再j的位置进行剪

3.剪多刀，则dp[i]=j*dp[i-j] 代表在j的地方剪一刀，剪完之后使用dp[i-j]

3.dp数组初始化

dp[2]=1*1=1

4.遍历顺序

从前向后遍历得到i，然后从0遍历i得到j

5.举例推导
'''
class Solution:
    def cuttingBamboo(self, bamboo_len: int) -> int:
        dp=[0]*(bamboo_len+1)#创建状态转移数组
        dp[2]=1#初始化
        for i in range(3,bamboo_len+1):#从前向后遍历得到i
            for j in range(i):#然后从0遍历i得到j
                dp[i]=max(dp[i],j*dp[i-j],j*(i-j))#按照递推公式进行计算
        return dp[-1]#返回结果
