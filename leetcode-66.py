给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

=============================================================================================

借鉴别人思路并改进

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s = s +str(i)
        print(s)
        s = str(int(s) + 1)
        print(s)
        return list(map(int, s)) ========置顶



========================================================================================
我的，弱 不对
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        for i, num in enumerate(digits):
            if int(num) != 9:
                digits[i] = 1 + int(num)
                print(digits)
                
            else:
                if num == digits[-1] and num == 9:
                    digits = '1' + '0'*len(digits)
                    return list(map(int, digits))
                else:
                    if int(num) == 9:
                        digits[i] = 0
                        print(digits)
                    continue
        digits.reverse()        
        return digits
                
