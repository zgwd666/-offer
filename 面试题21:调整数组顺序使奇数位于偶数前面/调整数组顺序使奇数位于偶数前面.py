#https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
'''
解题思路：采用快慢指针的思路，初始化快慢指针指向下标为0，此时快指针向右移动，如果找到了奇数，则将本位置与奇数的位置进行调换，然后慢指针+1
'''
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        if not actions:#太特殊情况
            return actions
        s,f=0,0#初始化快慢指针
        while f<len(actions):#当f没有遍历到终点
            if actions[f]%2==1:#找到奇数
                actions[s],actions[f]=actions[f],actions[s]#本位置进行置换
                s+=1#慢指针向前移动
            f+=1#快指针向前移动
        return actions#返回结果
