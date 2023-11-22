# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 0(nlogn n)
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
                #case of non overlapping
            else:
                output.append([start, end])
        return output

        