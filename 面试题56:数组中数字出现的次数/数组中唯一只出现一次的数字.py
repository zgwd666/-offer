#https://leetcode.cn/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/
'''
解题思路：采用哈希表存放每个数字出现的次数，然后将出现次数为1的数字添加到结果数组中
'''
class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        if len(actions)==1:#如果数组中仅存一个数字，直接返回即可
            return actions[0]
        hmap={}#初始化哈希表
        for action in actions:#对数组进行遍历，计算每个数字出现的次数
            if action not in hmap:
                hmap[action]=1
            else:
                hmap[action]+=1
        for value in hmap:#遍历哈希表，返回只出现一次的数字
            if hmap[value]==1:
                return value
        return -1#如果找不到只出现一次的数字，返回-1
