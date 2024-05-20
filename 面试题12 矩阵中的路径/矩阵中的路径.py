#https://leetcode.cn/problems/word-search/
'''
解题思路：
采用深度优先搜索的思路

对board数组进行遍历的时候，如果找到了word开头的第一个字母，则开始对该位置的四个方向上寻找下一个字母，如果找到了，则不断进行搜索查找，直到找到word中所含有的所有字母
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)#获得m
        n=len(board[0])#获得n
        dir=[(0,1),(1,0),(0,-1),(-1,0)]#创建方向数组
        visited=[[False for i in range(n)]for i in range(m)]#创建标识数组
        def dfs(board,visited,x,y,word,word_idx):#dfs函数，参数为board数组，标识数组，当前的点位坐标，word数组以及当前的word字母下标
            if word_idx==len(word):#当下标等于长度，证明可以找到，返回True
                return True
            for dx,dy in dir:#对当前点的四个方向进行寻找
                nextx,nexty=x+dx,y+dy#获取下一个点坐标
                if nextx<0 or nextx>=m or nexty<0 or nexty>=n or board[nextx][nexty]!=word[word_idx] or visited[nextx][nexty]:#如果下一个点的坐标超过边界或者已经访问过了或者不等于word中下一个字符，则直接跳过
                    continue
                visited[nextx][nexty]=True#如果满足条件，则将下一个点标记为访问
                if dfs(board,visited,nextx,nexty,word,word_idx+1):#对下一个点继续采用递归的方法，如果找到word，返回True
                    return True 
                else:#如果没有找到，则将下一个点的状态回退到未访问
                    visited[nextx][nexty]=False
            return False#没找到，返回False
        for i in range(m):#对每一个点进行遍历
            for j in range(n):
                if board[i][j]==word[0]:#如果找到了word的开头字母
                    visited[i][j]=True #先将当前点标记为已访问
                    if dfs(board,visited,i,j,word,1):#对当前点进行递归，满足条件返回True
                        return True
                    else:#不满足条件，回退该点的状态
                        visited[i][j]=False
        return False#整个数组不满足要求，返回False
