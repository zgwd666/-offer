#https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
'''
解题思路：采用双指针代替双层循环以缩短时间。

l,r分别指向数组的首末位元素。

当price[l]+price[r]>target证明相加过大，r-1

当price[l]+price[r]<target证明相加过小，l+1

相等则返回[price[l],price[r]]
'''
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        if price[0]>=target:#判断特殊情况
            return 
        l,r=0,len(price)-1#l,r分别指向数组的首末位元素。
        while l<r:#进行遍历，当l>r的时候停止，证明无解
            if price[l]+price[r]<target:#当price[l]+price[r]<target证明相加过小，l+1
                l+=1
            elif price[l]+price[r]>target:#当price[l]+price[r]>target证明相加过大，r-1
                r-=1
            else:#相等则返回[price[l],price[r]]
                return[price[l],price[r]]
        return [-1,-1]#没找到返回-1 -1
