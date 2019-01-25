def remove_duplicate(nums):
    if not nums:
        return

    if len(nums) == 0:
        return []

    i = 0
    hash = set([])
    while i < len(nums):
        if i < len(nums) and nums[i] not in hash:
            hash.add(nums[i])
            i += 1
        if i < len(nums) and nums[i] in hash:
            del nums[i]

    return nums

print(remove_duplicate([1, 0, 1, 1, 1]))

def generate_list(start, end, target):
    result = []
    helper = 1
    while True:
        if helper >= start and helper <= end:
            result.append(helper)
        if helper > end:
            break
        helper *= target

    return result

print(generate_list(2, 16, 2))


class ManageList:
    def __init__(self):
        self.result = []
        self.sum = 0
        self.record_number = {}
        self.most_member = None

    def insert(self, x):
        self.result.append(x)
        self.result.sort()
        self.sum = sum(self.result)
        if x not in self.record_number:
            self.record_number[x] = 1
        if x in self.record_number:
            self.record_number[x] += 1
        if self.most_member is None:
            self.most_member = x
        if self.most_member is not None and self.record_number[x] > self.most_member:
            self.most_member = x

    def get_max(self):
        if len(self.result) == 0:
            return
        return self.result[-1]

    def get_mean(self):
        if len(self.result) == 0:
            return
        return self.sum * 1.0 / len(self.result)

    def get_mode(self):
        return self.most_member

a = ManageList()

print(a.get_max())
print(a.get_mean())
print(a.get_mode())


