# [leetcode030] Substring with Concatenation of All Words解题报告

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

**Example 1:**

> **Input:**
>  s = "barfoothefoobarman",   
>  words = ["foo","bar"]   
> **Output: [0,9]**   
> Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.   
> The output order does not matter, returning [9,0] is fine too.   


**Example 2:**

> **Input:**   
>  s = "wordgoodstudentgoodword",
>  words = ["word","student"]  
> **Output: []**

## 题目大意
给定一个字符串s和一个由相同长度的单词组成的单词列表。从s中找到所有由单词列表中单词组成的子串，要求每个单词都被使用且仅被使用一次，子串中没有多余的字符，并返回所有的子串起始下标。


## 解题思路
题目中明确说了每个单词长度相同，因此每个单词等同于一个字符，遍历字符串时，每次移动间隔为单词长度。另一方面，与一个字符不同之处在于遍历字符串s一遍之后，需要将起始位置+1之后接着变量，总共需要变量次数为单词长度。以示例1为例，字符串"barfoothefoobarman"需要遍历3遍，分别如下：
1. 'bar' | 'foo' | 'the' | 'foo' | 'bar' | 'man'
2. 'arf' | 'oot' | 'hef' | 'oob' | 'arm'
3. 'rfo' | 'oth' | 'efo' | 'oba' | 'rma'
 
遍历时，需要两个指针，一个表示字符串匹配的起始位置，一个表示当前正在匹配的字符串位置。为了快速查找字符串是否在words中，需要用一个dict（words中单词可能有重复，不能用set，记为freq）来记录words中单词及其出现频数，同时用另一个dict（记为cntFreq）记录当前匹配的单词及其频数，为了简单需要引入另一个变量cnt表示当前匹配的总单词数。
1. 如果当前单词不在words中，则起始指针直接移至当前位置的下一个位置，同时清空cntFreq，并重置cnt为0。
2. 如果当前单词在words中，则将其加入cntFreq中，且cnt = cnt + 1。此时需要判断当前单词匹配的频数是否超过words中出现次数，如果超过了，起始位置不断的右移一个位置，直至出现次数相等。同时判断是否完全匹配。如果是，则输出当前起始位置，同时起始指针右移一个位置，该位置单词出现数-1，总匹配数-1,继续遍历。


```python
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
                # 字符串起始位置
                start = i
                # 记录当前词频
                cntFreq = {}
                # 已匹配的单词数
                cnt = 0
                for j in range(i, len(s) - wordLength + 1, wordLength):
                    next = s[j:j + wordLength]
                    # 如果单词在words中
                    if next in freq:
                        cntFreq[next] = cntFreq.get(next, 0) + 1
                        cnt += 1
                        # 单词出现频数超过了words中的频数，起始位置指针不断右移直至出现次数相等
                        while cntFreq[next] > freq[next]:
                            front = s[start:start + wordLength]
                            cntFreq[front] -= 1
                            cnt -= 1
                            start += wordLength
                        # 如果单词全部匹配，输出本次起始位置，同时移除第一个单词
                        if cnt == len(words):
                            res.append(start)
                            front = s[start:start + wordLength]
                            cntFreq[front] -= 1
                            cnt -= 1
                            start += wordLength
                    # 如果当前单词不在words中，起始指针直接移到当前下一个位置，同时清空匹配单词
                    else:
                        start = j + wordLength
                        cnt = 0
                        cntFreq.clear()
        return res
```