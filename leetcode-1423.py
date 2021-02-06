class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        N = len(cardPoints)
        preSum = [0] * (N + 1)
        for i in range(N):
            preSum[i + 1] = preSum[i] + cardPoints[i]
        res = float("inf")
        windowSize = N - k
        for i in range(k + 1):
            res = min(res, preSum[windowSize + i] - preSum[i])
        return preSum[N] - res
