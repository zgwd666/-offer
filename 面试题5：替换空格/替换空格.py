#https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
'''
解题思路：新建一个列表，用于在遍历过程中替换'.'，最后将列表转换为str
'''
class Solution:
    def pathEncryption(self, path: str) -> str:
        if not path:#判断特殊情况
            return path
        result=[]#初始化列表
        for p in path:#进行遍历
            if p=='.':#发现目标元素，进行替换
                result.append(' ')
            else:#不是目标元素。直接添加
                result.append(p)
        return ''.join(result)#返回列表转str的结果
