class Solution(object):
    def fizzbuzz(self, n: int):
        """
        :param n: 正整数
        :return:
        """
        output = []
        for i in range(1, n+1):
            if i % 15 == 0:
                output.append('FizzBuzz')
            elif i % 3 == 0:
                output.append('Fizz')
            elif i % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output


if __name__ == '__main__':
    print("leetcode 412")
    n = 18
    print(Solution().fizzbuzz(n))

