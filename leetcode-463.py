算周长说白了就是找边缘，找边缘说白了就是锐化，所以可以按照锐化的算法来算。


from scipy.signal import convolve2d
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return int(abs(convolve2d(grid,[[-2,1],[1,0]])).sum())
这个卷积核就是拉普拉斯算子[[0,-1,0],[-1,4,-1],[0,-1,0]]的一半，正负无所谓，只要异号就行，[[2,-1],[-1,0]]和[[-2,1],[1,0]]的结果是一样的。直接用拉普拉斯算子算也可以，不过因为拉普拉斯算子是二阶微分算子，每条边找了两次，所以结果要除2。

