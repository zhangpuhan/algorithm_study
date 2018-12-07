class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here

        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 != 0:
                ans.append("fizz")
                continue

            elif i % 5 == 0 and i % 3 != 0:
                ans.append("buzz")
                continue

            elif i % 5 == 0 and i % 3 == 0:
                ans.append("fizz buzz")
                continue

            else:
                ans.append(str(i))
                continue

        return ans