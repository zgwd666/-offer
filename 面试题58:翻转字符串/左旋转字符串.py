#https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
'''
解题思路：字符串切片，获取字符串 `password[target:]` 切片和 `password[:target]` 切片，使用 "+" 运算符拼接并返回即可。
'''
class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        front=password[:target]#获取前面的字符串
        back=password[target:]#获取后面的字符串
        result=back+front#进行拼接
        return result#返回结果
