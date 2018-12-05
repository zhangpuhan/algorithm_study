class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, S):
        # Write your code here

        answer = []

        i = 0

        while i < len(S):
            if not S[i].isalpha():
                if S[i] != " ":
                    answer.append(S[i])
                i += 1
                continue

            if S[i].isalpha():
                temp = ""
                while i < len(S) and S[i].isalpha():
                    temp += S[i]
                    i += 1
                answer.append(temp)
                continue

        return answer
