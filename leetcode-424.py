class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        # 动态滑动窗口
        maxLen, windowStart, maxFreq = 0, 0, 0
        # 统计出现频率
        freqDict = defaultdict(int)
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            freqDict[rightChar] += 1
            # 保存历史出现的最大频率
            maxFreq = max(freqDict[rightChar], maxFreq)
            # 缩小滑动窗口
            if (windowEnd - windowStart + 1 - maxFreq) > k:
                leftChar = s[windowStart]
                windowStart += 1
                freqDict[leftChar] -= 1       
            maxLen = max(maxLen, windowEnd - windowStart + 1)
        return maxLen
