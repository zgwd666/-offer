#https://leetcode.cn/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
'''
解题思路：
采用循环的方式将每个数组进行打印，从1开始，到10**cnt-1结束
'''
class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        res=[]#创建空的结果数组
        for i in range(1,10**cnt):#遍历，从1开始，到10**cnt-1结束
            res.append(i)#将数字加入数组中
        return res#返回结果数组
