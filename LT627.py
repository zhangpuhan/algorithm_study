class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        hash = {}

        for ch in s:
            if ch in hash:
                del hash[ch]
            else:
                hash[ch] = True

        remove = len(hash)

        if remove > 0:
            remove -= 1

        return len(s) - remove