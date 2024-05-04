#https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
'''
解题思路：我们可以采用哈希表的方式，在对数组元素进行遍历的过程中，将数组元素存入哈希表中，如果在过程中发现待存入的元素已经存在哈希表中，也就是发现了重复元素，直接返回即可。
'''
class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        dict1={}#初始化哈希表
        for document in documents:#进行遍历
            if document not in dict1:#如果元素不在哈希表中
                dict1[document]=1#将元素存入哈希表
            else:
                return document#待存入的元素已经存在哈希表中，也就是发现了重复元素，直接返回
        return -1#数组中不存在重复的元素
