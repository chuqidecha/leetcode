class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        count = len(strs)
        if count == 0:
            return ''

        prefix = ''
        cntStr1 = strs[0]
        for i in range(1, count):
            j = 0
            cntStr2 = strs[i]
            while j < len(cntStr1) and j < len(cntStr2):
                if cntStr1[j] != cntStr2[j]:
                    break
                else:
                    prefix += cntStr1[j]
                    j += 1
            cntStr1 = prefix
            prefix = ''
        return cntStr1 if len(cntStr1) > 0 else ''


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solution.longestCommonPrefix([]))
