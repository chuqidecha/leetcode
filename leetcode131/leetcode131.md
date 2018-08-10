# 131. Palindrome Partitioning
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

题目大意是将字符串从任意位置分割成多个子字符串，这些子字符串都是回文字符串。

这道题目需要采用深度优先遍历方法来遍历所有的解，同时判断每次划分后的子串是否时回文字符串。
深度优先遍历的复杂度是o(n^2),如果同时判断每个子字符串是否是回文字符串，整个算法的复杂度是o(n^3)。
为了降低时间复杂度，可以使用一个n×n的数组保存字符串s\[i:j\]是否时回文字符串，在o(1)的时间复杂度判断子字符串是否是回文字符串。

如果判断s\[i:j\]是否是回文字符串，有四种情况：
* i == j，则是回文字符串
* s\[i\] == s\[j\]且 i + 1  = j,则是回文字符串
* s\[i\] == s\[j\]且 s\[i+1\]\[j-1\]是回文字符串，则是回文字符串
* s\[i\] != s\[j\]则不是回文字符串

因此有递推公式：dp\[i\]\[j\] = s\[i\] == s\[j\] and (i == j or i + 1  = j or dp\[i+1\]\[j-1\])

采用动态规划求出所有的子字符串是否是回文字符串，再采用深度优先遍历求出所有可能的划分。此时算法的时间和空间复杂度都是o(n^2)。

```python
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        palindrome = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                palindrome[i][j] = s[i] == s[j] and (i == j or i + 1 == j or palindrome[i + 1][j - 1])

        return self.helper(s,0,palindrome,[])

    def helper(self, s, start, palindrome, item):
        if len(s) == start:
            return [item]
        items = []
        for i in range(start, len(s)):
            if palindrome[start][i]:
                cntItem = item[:]
                cntItem.append(s[start:i+1])
                items.extend(self.helper(s,i+1,palindrome,cntItem))

        return items
```