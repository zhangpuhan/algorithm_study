class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    nums = []

    def add(self, number):
        self.nums.append(number)

    def find(self, value):
        self.nums.sort()

        l, r = 0, len(self.nums) - 1

        while l < r:

            temp = self.nums[l] + self.nums[r]

            if temp == value:
                return True
            elif temp < value:
                l += 1
            else:
                r -= 1

        return False