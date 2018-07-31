#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-7-25 下午6:49
# @Author  : yinwb
# @File    : leetcode012.py
class Solution:
    def __remainderToRoman(self, remainder, cnt, half, next):
        '''
        :param remainder:
        :param cnt: str
        :param half: str
        :param next: str
        :return:
        '''
        if remainder < 4:
            roman = [cnt] * remainder
        elif remainder == 4:
            roman = [half, cnt]
        elif remainder == 5:
            roman = [half]
        elif remainder < 9:
            roman = [cnt] * (remainder - 5)
            roman.append(half)
        else:
            roman = [next, cnt]
        return roman

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rounds = 1
        roman = []
        while num != 0 or len(roman) == 0:
            remainder = num % 10
            num = num // 10
            rounds *= 10
            if remainder == 0:
                continue
            if rounds == 10:
                res = self.__remainderToRoman(remainder, 'I', 'V', 'X')
            elif rounds == 100:
                res = self.__remainderToRoman(remainder, 'X', 'L', 'C')
            elif rounds == 1000:
                res = self.__remainderToRoman(remainder, 'C', 'D', 'M')
            else:
                res = ['M'] * remainder
            roman.extend(res)

        roman.reverse()
        return ''.join(roman)


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(6))
    print(solution.intToRoman(4))
    print(solution.intToRoman(9))
    print(solution.intToRoman(50))
    print(solution.intToRoman(58))
    print(solution.intToRoman(1994))
