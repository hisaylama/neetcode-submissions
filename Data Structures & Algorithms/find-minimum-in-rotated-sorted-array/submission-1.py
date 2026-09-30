class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #nums = sorted(nums)
        #return nums[0]
        #Time complexity = O(nlogn)m space complexity = O(n)
        
        #Binary search method

        l, r = 0, len(nums)-1
        
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else: #nums[m] <= nums[r]:
                r = m 
        return nums[l]

        