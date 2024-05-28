#https://leetcode.cn/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/
'''
解题思路：利用一个栈存储添加的数字，然后采用一个变量计算当前的中位数

当加入数字时，对数组进行排序，然后计算当前数组的中位数
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]#用来存储数字
        self.mid=0#用来记录中位数


    def addNum(self, num: int) -> None:
        if len(self.stack)==0:#当数组为空时添加数字时，直接添加数字，中位数也是当前的数字
            self.stack.append(num)
            self.mid=num
        else:#当数组中已经存在数字时，保持数组的递增趋势，找到第一个大于当前数字的位置进行插入数字
            i=0
            while i<len(self.stack):
                if self.stack[i]<num:
                    i+=1
                else:
                    break
            self.stack.insert(i,num)
            n=len(self.stack)
            #当n为偶数时，计算中间两个数字的平均值，n为奇数，就是中间值
            if n%2==0:
                self.mid=(self.stack[n//2]+self.stack[n//2-1])/2
            else:
                self.mid=self.stack[n//2]

    def findMedian(self) -> float:
        if len(self.stack)==0:#当数组为空，返回None
            return None
        return self.mid#返回中间值
