from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        arr = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    arr[i] = max(arr[i], 1 + arr[j])
        return max(arr)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ### 贪心+二分
        if not nums:
            return 0
        n = len(nums)
        d = [nums[0]]
        lens = 1
        for i in range(1, n):
            if nums[i] > d[-1]:
                d.append(nums[i])
                lens += 1
            else:
                l, r = 0, lens - 1
                while l < r:
                    mid = (r - l) // 2 + l
                    if d[mid] >= nums[i]:
                        r = mid
                    else:
                        l = mid + 1
                d[r] = nums[i]
        return lens


class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        helper = []
        for x in nums:
            if not helper or x > helper[-1]:
                helper.append(x)
            else:
                pos = bisect_left(helper, x)
                helper[pos] = x
        return len(helper)


s = Solution()
res = s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print(res)
