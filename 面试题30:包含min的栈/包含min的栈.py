#https://leetcode.cn/problems/bao-han-minhan-shu-de-zhan-lcof/
'''
解题思路：主要采用两个栈来实现，一个栈用来实现正常的栈的功能，一个栈用来记录最小值
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #初始化两个栈，一个用来实现正常栈功能，一个用来记录最小值
        self.stack=[]
        self.min=[]

    def push(self, x: int) -> None:
        #元素入栈时，栈1元素正常入栈，最小值栈为空或者带入栈元素比栈中的最小值更小时，待入栈元素入最小值栈
        self.stack.append(x)
        if not self.min or self.min[-1]>=x:
            self.min.append(x)

    def pop(self) -> None:
        #元素出栈时，栈1元素正常出栈，当出栈元素等于最小值栈的最小值时，最小值栈的栈顶元素也出栈
        if self.stack.pop()==self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        #查看顶部元素功能，返回栈1的栈顶元素
        return self.stack[-1]
        
    def getMin(self) -> int:
        #获取最小值功能，返回最小值栈的栈顶元素
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
