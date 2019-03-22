# 题解里的 除10 取余的 算法思路没太懂
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            list_x = list(str(x))
            list_x.reverse() # 关于reverse() 的理解也出错了
            for i in range(len(list_x)):
                if list(str(x))[i] != list_x[i]:
                    return False
                else:
                    if i != (len(list_x)-1): # 这里出错了
                        continue
                    else:
                        return True
            
