#https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
'''
解题思路：
考虑使用一个辅助栈stack，模拟放入/拿去操作的排列。根据是否模拟成功，即可得到结果。

- 入栈操作：按照每次压栈的顺序执行
- 出栈操作：每次入栈后，循环判断“栈顶元素==拿取序列的当前元素是否成立”，将符合拿取序列顺序的栈顶元素全部拿取

算法流程：

初始化;辅助栈stack，拿取索引的序列i

遍历压栈元素：各元素记为num 

​	元素num入栈

​	循环出栈：若stack的栈顶元素==拿取元素takeOut[i]，则执行出栈与i++

返回值：若stack为空，则此拿取序列合法
'''
class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        stack=[]#创建一个空栈
        index=0#初始化索引为0
        for num in putIn:#对压入栈的每个数字进行遍历
            stack.append(num)#将数字加入辅助栈中
            while stack and stack[-1]==takeOut[index]:#循环出栈：若stack的栈顶元素==拿取元素takeOut[i]，则执行出栈与i++
                stack.pop()
                index+=1
        return not stack#如果辅助栈为空则代表可以，否则就不行
