#https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
'''
解题思路：
两个栈实现队列，按照题意，主要实现入队和出队的操作。
可以使用两个栈，一个栈只用于入队，一个栈只用于出队。
在入队时，将元素添加到入队A栈中。
在出队时，首先判断入队栈A和出队栈B中是否存在元素，如果都不存在，返回-1.
如果出队栈B中存在元素，直接弹出即可。
否则先将入队栈A中的元素出栈，然后将出栈的元素入栈到出队栈B中，这样出队栈B出栈时就是先入A的先出B。
'''
class CQueue:

    def __init__(self):
        self.stack_in=[]#只用于入队的栈
        self.stack_out=[]#只用于出队的栈

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)#入栈
    def deleteHead(self) -> int:
        if len(self.stack_in)==0 and len(self.stack_out)==0:#如果两个栈中都没有元素，此时出栈返回-1
            return -1
        else:#两个栈中至少有一个
            if self.stack_out:#出队栈中存在元素，直接弹出
                return self.stack_out.pop()
            else:#出队栈中不存在元素
                while self.stack_in:#将入队栈中的元素存入出队栈中
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()#出队栈进行出队



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
