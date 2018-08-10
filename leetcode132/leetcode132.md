# 132. Palindrome Partitioning II
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

**Eaxmple:**

> **Input:**"aab"
>
> **Output:**
>
> \[
>
> &nbsp;&nbsp; \["aa","b"\],
>
> &nbsp;&nbsp; \["a","a","b"\]
>
> \]

## 解题思路

这道题目与[131. Palindrome Partitioning](../leetcode131/leetcode131.md)类似。
不同之处是不需要输出分割方式，而仅仅需要最小分割次数。最简单的方法是深度优先遍历所有的解，然后求出最小分割次数。

```python
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindrome = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                palindrome[i][j] = s[i] == s[j] and (i == j or i + 1 == j or palindrome[i + 1][j - 1])

        return self.helper(s,0,palindrome,[])

    def helper(self, s, start, palindrome, item):
        if len(s) == start:
            return len(item) - 1
        times = len(s)
        for i in range(start, len(s)):
            if palindrome[start][i]:
                cntItem = item[:]
                cntItem.append(s[start:i+1])
                times = min(self.helper(s,i+1,palindrome,cntItem),times)

        return times
```
但是很不幸，这种方式虽然没有问题，但是复杂度太高，会出现Time Limit Exceeded。
对于字符串相关的问题如果要求输出所有的解一般使用DFS，但如果仅仅是输出解的数目或者其他，
一般采用动态规划的方式。

动态规划方法最重要的步骤就是找递推公式和设置初值。如果用数组dp\[i\]表示字符串s\[i:\]最小分割次数，则
dp\[i\] = min(len(s\[i:\],dp\[j+1\] + 1),其中 i<= j < len(s)

如果s\[i:j\]是回文字符串，则从j处进行分割将s\[i:\]分割成回文字符串的次数等于dp\[j+1\] + 1。
对于初值，分割的最大次数显然是字符串的长度-1。

```python
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindrome = [[False] * len(s) for _ in range(len(s))]
        dp = list(range(len(s) - 1, -2, -1))

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s) - 1, i - 1, -1):
                palindrome[i][j] = s[i] == s[j] and (i == j or i + 1 == j or palindrome[i + 1][j - 1])

                if palindrome[i][j]:
                    dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0]

```