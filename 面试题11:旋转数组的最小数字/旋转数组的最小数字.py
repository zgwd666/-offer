#https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
'''
解题思路：二分法

采用两个指针，l,r分别指向数组的首尾数字，然就计算两个指针之间的中间索引值，然后可能遇到如下三种情况：

1.mid<r:代表最小值一定在mid的左侧或者就是mid，所以r移动到mid位置

2.mid>r:代表最小值一定在mid右侧，将l移动到mid+1的位置

3.mid=r:代表最小值可能在mid左侧也可能在mid右侧，只能通过r指针递减，实现寻找最小值
'''
class Solution:
    def stockManagement(self, stock: List[int]) -> int:
        if len(stock)==1:#判断特殊情况
            return stock[0]
        l,r=0,len(stock)-1#初始化左右指针
        while l<r:#进行遍历
            mid=(r-l)//2+l#计算中间指针
            if stock[mid]>stock[r]:#第二种情况
                l=mid+1#将l移动到mid+1的位置
            elif stock[mid]<stock[r]:#第一种情况
                r=mid#r移动到mid位置
            else:#第三种情况
                r=r-1#r指针递减，实现寻找最小值
        return stock[l]#返回最小值
