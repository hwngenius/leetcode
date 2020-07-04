class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        index,length=0,len(intervals)
        ans=[]
        while index<length and newInterval[0]>intervals[index][0]:
            ans.append(intervals[index])
            index+=1
        if len(ans)==0:
            ans.append(newInterval)
        if ans[-1][1]>=newInterval[0]:
            ans[-1][1]=max(newInterval[1],ans[-1][1])
        else:
            ans.append(newInterval)
        while index < length and ans[-1][1] >= intervals[index][0]:
            ans[-1][1] = max(ans[-1][1], intervals[index][1])
            index += 1
        while index<length:
            ans.append(intervals[index])
            index+=1
        return ans

# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 98.66%
# 的用户
# 内存消耗：
# 15.2 MB
# , 在所有 Python3 提交中击败了
# 100.00%
# 的用户
