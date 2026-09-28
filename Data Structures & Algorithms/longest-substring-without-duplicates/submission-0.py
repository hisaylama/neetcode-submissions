class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Use set() instead of ()
        l = 0
        maxLen = 0

        for r in range(len(s)):
            # If we hit a duplicate, shrink the window from the left
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)

        return maxLen 