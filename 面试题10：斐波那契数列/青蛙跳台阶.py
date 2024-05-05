#https://leetcode.cn/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/
'''
解题思路：采用回溯的基本思路
通过数学归纳可知，规律为f(n)=f(n-1)+f(n-2)
并且f(0)=f(1)=1
'''
from functools import lru_cache#内置缓存器，减少重复计算，提升性能
class Solution:
    @lru_cache(None)
    def trainWays(self, num: int) -> int:
        if num<2:#初始化f(0)和f(1)
            return 1
        return (self.trainWays(num-1)+self.trainWays(num-2))%1000000007#根据公式进行回溯
