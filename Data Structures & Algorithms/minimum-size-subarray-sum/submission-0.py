class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        min_length = n+1

        for i in range(n):
            current_sum = 0

            for j in range(i, n):
                current_sum += nums[j]

                if current_sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break
        return min_length if min_length <= n else 0

       
    