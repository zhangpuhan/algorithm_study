class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        # write your code here

        answer = [""]

        for ch in S:
            if ch.isalpha():
                answer = [i+j for i in answer for j in [ch.lower(), ch.upper()]]
                continue

            else:
                answer = [i+ch for i in answer]


        return answer
