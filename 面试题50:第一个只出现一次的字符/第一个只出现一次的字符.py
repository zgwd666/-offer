#https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
'''
解题思路：采用哈希表存储顺序存储数组中每个元素出现的次数，然后遍历哈希表，找到第一个次数为1的元素即可。
'''
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        if len(arr)==0:#当数组为空，直接返回空格
            return ' '
        dict1={}#初始化哈希表
        for i in range(len(arr)):#对数组中每个元素进行遍历，按顺序记录下它们出现的次数
            if arr[i] not in dict1:
                dict1[arr[i]]=1
            else:
                dict1[arr[i]]+=1
        for key in dict1:#对哈希表进行遍历，找到第一个次数为1的元素，进行返回
            if dict1[key]==1:
                return key
        return ' '#找不到非重复的元素，直接返回空格
