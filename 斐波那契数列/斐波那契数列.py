#https://leetcode.cn/problems/fei-bo-na-qi-shu-lie-lcof/
'''
解题思路：可以采用回溯的方式，但是由于回溯的重复计算，会导致时间溢出，本题采用动态规划的方法进行计算，dp[i]代表下标为i的斐波那契数列中的数值，递推公式为F(n) = F(n - 1) + F(n - 2),初始化dp[0]=0,dp[1]=1；遍历顺序从前向后即可
'''
class Solution:
    def fib(self, n: int) -> int:
        if n<2:#当n为0和1时，数值等于本身
            return n
        dp=[0]*(n+1)#初始化状态转移数组
        dp[1]=1#初始化dp[1]
        for i in range(2,n+1):#进行遍历
            dp[i]=dp[i-1]+dp[i-2]#按照递推公式进行计算
        return dp[n]% 1000000007#返回结果
