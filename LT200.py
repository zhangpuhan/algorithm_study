class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return s

        chars = s
        chars = "#".join(chars)
        chars = "#" + chars + "#"

        par = [0 for _ in range(len(chars))]
        par[0] = 1

        mid, longest = 0, 1

        for i in range(1, len(chars)):
            length = 1
            if mid + longest > i:
                mirror = mid - (i - mid)
                length = min(par[mirror], mid + longest - i)

            while i + length < len(chars) and i - length >= 0:
                if chars[i + length] != chars[i - length]:
                    break
                length += 1

            if length > longest:
                longest = length
                mid = i

            par[i] = length

        longest = longest - 1
        start = (mid - 1) // 2 - (longest - 1) // 2
        return s[start:start + longest]