class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def setRoot(x, r=None):
            if x == bcj[x]:
                bcj[x] = x
                if r is not None:
                    bcj[x] = r
                    if r != x:
                        nonlocal m
                        m += 1
                    return r
                else:
                    return x
            else:
                bcj[x] = setRoot(bcj[x], r)
                return bcj[x]

        A, B, num_l, bcj, m = [], [], len(edges), list(range(n)), 1
        for t, x, y in edges:
            if t == 1:
                A.append((x - 1, y - 1))
            elif t == 2:
                B.append((x - 1, y - 1))
            else:
                setRoot(x - 1, setRoot(y - 1))
                if n == m:
                    return num_l - n + 1

        re_m, re_bcj = m, bcj.copy()
        for x, y in A:
            setRoot(x, setRoot(y))
            if n == m:
                break
        if n != m:
            return -1
        m, bcj = re_m, re_bcj
        for x, y in B:
            setRoot(x, setRoot(y))
            if n == m:
                return num_l - 2 * n + 1 + re_m
        return -1

