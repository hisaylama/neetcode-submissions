class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(i, size):
            # Push nums[i] down until the max-heap property holds
            while True:
                largest = i
                l, r = 2 * i + 1, 2 * i + 2
                if l < size and nums[l] > nums[largest]:
                    largest = l
                if r < size and nums[r] > nums[largest]:
                    largest = r
                if largest == i:
                    return
                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        # 1. Build max-heap: O(n)
        for i in range(n // 2 - 1, -1, -1):
            sift_down(i, n)

        # 2. Move max to the end, then shrink the heap: O(n log n)
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(0, end)

        return nums
            

        