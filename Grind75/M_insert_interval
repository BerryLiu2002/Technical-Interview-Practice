"""
Question Name: 57. Insert Interval
Difficulty: Medium
Category: Array
Link: https://leetcode.com/problems/insert-interval/
"""

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        pos = len(intervals)
        for i in range(len(intervals)):
            s, e = intervals[i]
            ns, ne = newInterval
            if ns < s:
                pos = i
                break
        intervals.insert(pos, newInterval)
        res = [intervals[0]]
        for each in intervals[1:]:
            ps, pe = res[-1]
            s, e = each
            if s <= pe:
                if e > pe:
                    res[-1][1] = e
            else:
                res.append(each)
        return res