class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        arr,res=list(goods),[]#初始化good和结果
        def dfs(x):#dfs函数
            if x==len(arr)-1:#当位置到最后一个位置，则直接返回结果
                res.append(''.join(arr))
                return
            hmap=set()#初始化一个set，用来去重
            for i in range(x,len(arr)):#进行遍历
                if arr[i] in hmap:continue#去重
                hmap.add(arr[i])#将元素加入到set中，用于进一步的去重
                arr[x],arr[i]=arr[i],arr[x]#交换位置
                dfs(x+1)#对下一个位置进行递归
                arr[x],arr[i]=arr[i],arr[x]#将位置交换回来
        dfs(0)#进行dfs
        return res#返回结果
