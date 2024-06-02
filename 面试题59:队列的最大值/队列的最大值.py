#https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/
'''
解题思路：使用两个队列实现功能，栈A用来实现正常的队列进队出队的功能，栈B用来存储当前栈中的最大值。
'''
class Checkout:

    def __init__(self):
        self.stack=[]#栈用来实现队列的基本功能
        self.max=[]#用来存储当前栈中的最大值


    def get_max(self) -> int:
        if len(self.stack)==0:#当队列为空，返回-1
            return -1
        return self.max[0]#队列有值，返回当前的最大值


    def add(self, value: int) -> None:
        self.stack.append(value)#将值进队
        while self.max and self.max[-1]<value:#当最大值栈有值且最大值栈的最后有一个数字比当前的值小，一直弹出，知道最大值栈的最后一个值不小于当前的值
            self.max.pop()
        self.max.append(value)#将当前的值加入到栈的最后一个数字

    def remove(self) -> int:
        if len(self.stack)==0:#当队列为空，返回-1
            return -1
        prices=self.stack.pop(0)#队列出队
        if prices==self.max[0]:#当出队的值等于最大值栈的第一个值，将最大值栈的第一个值也出栈
            self.max.pop(0)
        return prices#返回出队的值



# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
