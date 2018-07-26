class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        cntNums = {}
        for index, num in enumerate(nums):
            cnt = target - num
            if cnt in cntNums:
                return (cntNums[cnt], index)
            else:
                cntNums[num] = index


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
