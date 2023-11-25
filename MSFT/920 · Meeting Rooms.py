# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        return True


intervals = [[1, 3], [4, 6], [7, 9]]
solution_instance = Solution()
result = solution_instance.canAttendMeetings(intervals)
print(result)