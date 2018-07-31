#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-29 下午1:38
# @Author  : yinwb
# @File    : leetcode046.py

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        rLists = []
        for index, num in enumerate(nums):
            nextNums = nums[:]
            del nextNums[index]
            nextLists = self.permute(nextNums)
            for nextList in nextLists:
                nextList.append(num)
                rLists.append(nextList)
        return rLists


if __name__ == "__main__":
   solution = Solution()
   print(solution.permute([1,2,3]))