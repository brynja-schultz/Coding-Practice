class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pal = "".join(char.lower() for char in s if char.isalnum())

        if not pal:
            return True

        left = 0
        right = len(pal) - 1

        for i in range (len(pal)//2):
            if pal[left] != pal[right]:
                return False
            left += 1
            right -= 1

        return True
