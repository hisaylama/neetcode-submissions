from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        # @cache
        # def dfs(i):
        #     if i>=n:
        #         return i == n
        #     return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5)/2
        psi = (1 - sqrt5)/2

        n += 1
        
        return round((phi**n - psi**n)/ sqrt5) 
