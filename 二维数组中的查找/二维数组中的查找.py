#https://leetcode.cn/problems/search-a-2d-matrix-ii/
'''
解题思路：
根据矩阵的特点，可以知道右上角的值是本行中最大的值，也是本列中最小的值，那么就可以根据矩阵的右上角的值进行行列的筛选。
如果右上角的值大于target，则证明本列的所有值都比target大，那么就将本列剔除
如果右上角的值小于target，则证明本行的所有制都比target小，那么将本行剔除
如果右上角的值等于target，则返回True
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:#判断特殊情况
            return False
        m=len(matrix)#提取矩阵的行数
        n=len(matrix[0])#提取矩阵的列数
        row=0#初始化行
        col=n-1#初始化列
        while row<m and col>=0:#进行遍历
            if matrix[row][col]>target:#如果右上角的值大于target，则证明本列的所有值都比target大，那么就将本列剔除
                col-=1
            elif matrix[row][col]<target:#如果右上角的值小于target，则证明本行的所有制都比target小，那么将本行剔除
                row+=1
            else:#如果右上角的值等于target，则返回True
                return True 
        return False#没有找到返回False
