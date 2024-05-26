#https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
'''
解题思路：采用哈希表来存储遍历过的数字出现的次数，如果发现某个数字出现的次数大于一半，直接返回就可以。
'''
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        if len(stock)==1:#如果只有一个元素，那就是众数
            return stock[0]
        dict1={}#初始化哈希表
        length=len(stock)//2#计算数组元素的一半
        for i in stock:#进行遍历
            #存储出现的次数
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
            if dict1[i]>length:#如果出现的次数超过一半，则就是众数
                return i
        return -1#找不到众数，返回-1
