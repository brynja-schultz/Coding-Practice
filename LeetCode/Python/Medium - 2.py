class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        left = 0
        seen = set()
        for idx in range(len(s)):
            while s[idx] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[idx])
            if len(seen) > longest:
                longest = len(seen)
        return longest
