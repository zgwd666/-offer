#https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
'''
解题思路：采用快速排序对数组进行排序，然后取排序后的数组前cnt个数字即可
'''
class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        if len(stock)<cnt or cnt==0:#判断特殊情况
            return []
        def quickSort(stock):#快排
            if len(stock)<=1:#当列表中小于一个数字就不要排序直接返回
                return stock
            pivot=stock[0]#取数组的第一个元素为基准
            less=[]#初始化小于数组和大于数组
            greater=[]
            for i in range(1,len(stock)):#遍历数组，将大于基准数的数字加入大于数组，其他数字加入小于数组
                if stock[i]>pivot:
                    greater.append(stock[i])
                else:
                    less.append(stock[i])
            return quickSort(less)+[pivot]+quickSort(greater)#递归进行排序
        sortStock=quickSort(stock)#进行快排
        return sortStock[:cnt]#然后取排序后的数组前cnt个数字即可
