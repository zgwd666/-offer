#https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
'''
解题思路：采用BFS的思想，对数组的每一个位置进行搜索，满足条件的位置进行标记且结果加一，最终返回结果即可
'''
class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        visited=[[False for i in range(n)]for i in range(m)]#初始化标记数组
        dir=[(0,1),(1,0)]#创建方向数组
        def digit(x,y):#计算点位各个位置上的数字和
            s=0
            while x!=0:
                s+=x%10
                x=x//10
            while y!=0:
                s+=y%10
                y=y//10
            return s
        def bfs(visited,i,j,cnt):#bfs函数，参数包括标记数组，点位坐标，cnt
            queue=[]#初始化队列
            queue.append((i,j))#将当前点加入队列中
            visited[i][j]=True#将当前点标记为True
            res=1#初始化结果未1
            while queue:#对队列进行遍历
                curx,cury=queue.pop()#弹出队列最左侧的点
                for dx,dy in dir:#对点的右侧和下侧点进行遍历
                    nextx,nexty=curx+dx,cury+dy#计算下一个点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n or visited[nextx][nexty] or digit(nextx,nexty)>cnt:#如果下一个点超过边界或者下一个点已经遍历过或者下一个点的和大于目标值，直接跳过
                        continue
                    res+=1#满足条件结果加一
                    visited[nextx][nexty]=True#将下一个点进行标记
                    queue.append((nextx,nexty))#将下一个点加入队列中
            return res#返回结果
        res=bfs(visited,0,0,cnt)#进行BFS计算结果
        return res#返回结果
