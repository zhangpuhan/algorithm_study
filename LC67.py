class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        la = len(a)
        lb = len(b)
        l = max(la, lb)

        a = a[::-1]
        b = b[::-1]

        if la > lb:
            b =  b + (la-lb)*"0"

        if la < lb:
            a =  a + (lb-la)*"0"

        result = ""

        residue = 0

        for i in range(l):
            addnow = int(a[i]) + int(b[i]) + residue

            if addnow == 0:
                result = "0" + result
                residue = 0

            if addnow == 1:
                result = "1" + result
                residue = 0

            if addnow == 2:
                result = "0" + result
                residue = 1

            if addnow == 3:
                result = "1" + result
                residue = 1

        if residue == 1:
            result = "1" + result

        return result
