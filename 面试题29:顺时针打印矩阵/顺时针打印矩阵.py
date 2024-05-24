#https://leetcode.cn/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
'''
解题思路：
顺时针打印数组的顺序是从左到右、从上到下、从右到左、从下到上的循环。
算法流程：
1.空值处理：当输入的array为空时，直接返回空列表[]即可
2.初始化：初始化矩阵的左、右、上、下四个边界l,r,t,b，以及结果列表res
3.循环打印：按照从左到右、从上到下、从右到左、从下到上四个方向循环打印
​	根据边界打印，即将元素按顺序添加到列表res尾部
​	边界向内收缩1
​	判断边界是否相遇，若打印完毕则跳出
4.返回值：返回res即可
'''
class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array:#空数组直接返回空列表
            return []
        l,r=0,len(array[0])-1#初始化左右边界
        t,b=0,len(array)-1#初始化上下边界
        res=[]#初始化结果
        while True:#进行遍历
            for i in range(l,r+1):#从左到右
                res.append(array[t][i])
            t+=1#上边界下移
            if t>b:break#如果边界相遇，则直接退出
            for i in range(t,b+1):#从上到下
                res.append(array[i][r])
            r-=1#右边界左移
            if l>r:break#如果边界相遇，则直接退出
            for i in range(r,l-1,-1):#从右到左
                res.append(array[b][i])
            b-=1#下边界上移
            if t>b:break#如果边界相遇，则直接退出
            for i in range(b,t-1,-1):#从下到上
                res.append(array[i][l])
            l+=1#左边界右移
            if l>r:break#如果边界相遇，则直接退出
        return res#返回遍历结果
