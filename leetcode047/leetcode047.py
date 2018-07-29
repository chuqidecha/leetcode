#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-29 下午2:07
# @Author  : yinwb
# @File    : leetcode047.py

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []
        nums = sorted(nums)
        return self.helper(nums, [], [False] * len(nums))

    def helper(self, nums, item, visited):
        if len(item) == len(nums):
            return [item]
        else:
            items = []
            for i in range(len(nums)):
                if (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]) or visited[i]:
                    continue
                else:
                    nextItem = item[:]
                    nextItem.append(nums[i])
                    nextVisited = visited[:]
                    nextVisited[i] = True
                    items.extend(self.helper(nums, nextItem, nextVisited))
            return items


if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([3, 3, 0, 3]))
