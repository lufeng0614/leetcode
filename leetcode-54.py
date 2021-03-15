class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        Row = len(matrix)
        if Row == 0:    return []
        Col = len(matrix[0])
        visited = [[False for _ in range(Col)] for _ in range(Row)]
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        res = []
        r, c = 0, 0
        di = 0
        for _ in range(Row * Col):
            res.append(matrix[r][c])
            visited[r][c] = True
            nr = r + dirs[di][0]
            nc = c + dirs[di][1]
            if 0<= nr < Row and 0<= nc < Col and visited[nr][nc]==False:
                r = nr
                c = nc
            else:           #如果碰壁了
                di = (di + 1) % 4       #要右转弯
                r = r + dirs[di][0]
                c = c + dirs[di][1]
        return res
