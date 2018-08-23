#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-8-23 下午9:28
# @Author  : yinwb
# @File    : leetcode030.py
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if len(s) > 0 and len(words) > 0:
            # words中的单词统计频数
            freq = {}
            for word in words:
                freq[word] = 1 + freq.get(word, 0)


            wordLength = len(word)
            for i in range(wordLength):
                start = i
                # 记录当前词频
                cntFreq = {}
                # 已匹配的单词数
                cnt = 0
                for j in range(i, len(s) - wordLength + 1, wordLength):
                    next = s[j:j + wordLength]
                    if next in freq:
                        cntFreq[next] = cntFreq.get(next, 0) + 1
                        cnt += 1
                        while cntFreq[next] > freq[next]:
                            front = s[start:start + wordLength]
                            cntFreq[front] -= 1
                            cnt -= 1
                            start += wordLength
                        if cnt == len(words):
                            res.append(start)
                            front = s[start:start + wordLength]
                            cntFreq[front] -= 1
                            cnt -= 1
                            start += wordLength
                    else:
                        start = j + wordLength
                        cnt = 0
                        cntFreq.clear()
        return res
if __name__ == '__main__':
    print(Solution().findSubstring("aaa",["aa","aa"]))
