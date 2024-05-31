#https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
'''
解题思路：采用哈希表存放每个数字出现的次数，然后将出现次数为1的数字添加到结果数组中
'''
class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        if len(sockets)==2:#当数组中仅有两个数字，直接返回即可
            return sockets
        dict1={}#初始化哈希表
        for socket in sockets:#对数组进行遍历，计算每个数字出现的次数
            if socket not in dict1:
                dict1[socket]=1
            else:
                dict1[socket]+=1
        res=[]#初始化结果数组
        for value in dict1:#遍历哈希表，将出现次数为1的数字在加入结果数组
            if dict1[value]==1:
                res.append(value)
        return res#返回结果
