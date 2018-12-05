class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        # Write your code here
        x = int(a, k)
        y = int(b, k)

        ans = int(x + y)
        s = ""

        while ans > 0:
            s = s + str(ans % k)
            ans = ans // k

        return s[::-1]
