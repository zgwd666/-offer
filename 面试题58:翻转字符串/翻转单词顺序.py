#https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/
'''
解题思路：
双指针算法。

倒序遍历字符串message，记录单词的左右边界i,j

每确定一个单词的边界，则将其添加到单词列表res

最终，将单词列表拼接为字符串，并返回即可
'''
class Solution:
    def reverseMessage(self, message: str) -> str: 
        message=message.strip()#删除前后的空格
        if len(message)==0:#判断特殊情况
            return ''
        i,j=len(message)-1,len(message)-1#初始化左右边界
        res=[]#初始化单词列表
        while i>=0:#遍历
            while i>=0 and message[i]!=' ':i-=1#当没有找到第一个单词的边界，i一直向前移动
            res.append(message[i+1:j+1])#将单词加入到列表中
            while i>=0 and message[i]==' ':i-=1#开始找第下个单词
            j=i#将j定位到i当前的位置
        return ' '.join(res)#将列表转为字符串
