class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset = set()

        # for num in nums:
        #     if num in hashset:
        #         return True
        #     hashset.add(num)
        # return False
        
        #Brute force 
        nums.sort() 
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return(True)
        return(False)

            

            
            
        