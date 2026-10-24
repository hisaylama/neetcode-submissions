class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Brute Force Scheme
        # n = len(nums)
        # min_length = n+1

        # for i in range(n):
        #     current_sum = 0

        #     for j in range(i, n):
        #         current_sum += nums[j]

        #         if current_sum >= target:
        #             min_length = min(min_length, j - i + 1)
        #             break

        # return min_length if min_length <= n else 0

        #Sliding Window

        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                res = min(r-l+1, res)
                total -= nums[l]
                l += 1

        return 0 if res == float("inf") else res



       
    