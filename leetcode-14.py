编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

=====================================================================

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        """
        时间复杂度你想象不到，短小精悍。
        1、利用python的max()和min()，在Python里字符串是可以比较的，
        按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
        2、 利用python的zip函数，把str看成list然后把输入看成二维数组，左对齐纵向压缩，然后把每项利用集合去重，
        之后遍历list中找到元素长度大于1之前的就是公共前缀
        """
        ************************************************************
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
        ************************************************************     
       
      def longestCommonPrefix(self, strs):
          if not strs: return ""
          ss = list(map(set, zip(*strs)))
          res = ""
          for i, x in enumerate(ss):
              x = list(x)
              if len(x) > 1:
                  break
              res = res + x[0]
          return res
        
        ************************************************************     
                
#         print(len(min(strs, key=lambda x: len(x))))
#         if len(strs) == 0:
#             return ''
#         elif: (min(strs, key=lambda x: len(x))) is '':
#             return ''
#         # elif: list(min(strs, key=lambda x: len(x)))[0] == s[0] for s in strs
#         #     return ''
#         else:
#             y = []
#             for i, s in enumerate(strs):
#                 tmp = min(strs, key=lambda x: len(x))
#                 tmp_l = list(tmp)
#                 for i, s in enumerate(strs):
#                     rus = ""
#                     for x, sm in enumerate(tmp_l):
#                         if s[x] == tmp_l[x]:
#                             rus = rus + sm
#                         y.append(rus)
#                 result = min(y, key=lambda a: len(a))
                    
#                 return result
                
        
            
            
