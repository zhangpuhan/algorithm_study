class Solution:
    """
    @param num: the number of "1"s on a given timetable
    @return: all possible time
    """

    def binaryTime(self, num):
        # Write your code here

        time = []
        hour = [[], [], [], []]
        mins = [[], [], [], [], [], []]

        for i in range(12):
            n = bin(i).count("1")
            hour[n].append(i)

        for i in range(60):
            n = bin(i).count("1")
            mins[n].append(i)

        for i in range(num + 1):
            if i < 4 and num - i < 6:
                for h in hour[i]:
                    for m in mins[num - i]:
                        time.append("%d:%02d" % (h, m))

        return time