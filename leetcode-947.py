class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # 建立访问的记录池
        visit = set()
        # 行列上都有哪些石头的索引
        lines = defaultdict(set)
        colums = defaultdict(set)
        for i in range(len(stones)):
            l, c = stones[i]
            lines[l].add(i)
            colums[c].add(i)
        res = 0
        pre = 0
        # 深度遍历联通的石头
        def dfs(x):
            line, colum = stones[x]
            visit.add(x)  # 访问过的元素，加入到已经访问的集合中
            for i in lines[line]:
                if i not in visit:
                    dfs(i)
            for i in colums[colum]:
                if i not in visit:
                    dfs(i)
        for i in range(len(stones)):
            if i not in visit:
                dfs(i)
                # 这里是利用访问过的集合数量，和之前的集合做差，得到本次访问联通量
                # 集合数量差-1，是因为减去出发时候的那个石头
                res += len(visit)-pre-1  
                pre = len(visit)  # 记录已访问元素个数，已被下次使用
        return res

  
