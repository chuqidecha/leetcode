# 115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.   

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

**Example 1:**

> Input: S = "rabbbit", T = "rabbit"   
> Output: 3   
> Explanation:   

> As shown below, there are 3 ways you can generate "rabbit" from S.   
> (The caret symbol ^ means the chosen letters)   

> rabbbit   
> ^^^^ ^^   
> rabbbit   
> ^^ ^^^^   
> rabbbit   
> ^^^ ^^^   

**Example 2:**

> Input: S = "babgbag", T = "bag"   
> Output: 5   
> Explanation:   

> As shown below, there are 5 ways you can generate "bag" from S.   
> (The caret symbol ^ means the chosen letters)   
 
> babgbag   
> ^^ ^   
> babgbag
> ^^    ^
> babgbag   
> ^    ^^   
> babgbag   
>   ^  ^^   
> babgbag   
>     ^^^

**解题思路1:深度优先搜索**
逐个比较s中的字符是否和t的首字母相等，如果相等，假设s[i] = t[0],则递归求s[i+1:]中有多少个不同的子序列等于t[1:]，直至t为空或者s的长度小于t的长度。

```python
class Solution:
    def numDistinct(self, s, t):
        if len(t) == 0:
            return 1
        if len(s) < len(t):
            return 0
        total = 0
        for i, si in enumerate(s):
            if si == t[0]:
                total += self.numDistinct2(s[i + 1:], t[1:])
        return total
```
这种算法复杂度很高，最坏情况下s与t分别为m、n(m>n)个相同字符c，则复杂度为$C_{m}^{n}$

**结题思路2：动态规划法**
用dp[i][j]表示s[:i]中子序列等于t[:j]的数目，如果s[i]和t[j]不想等，s[:i]中子序列等t[:j]的数目的数目应该是s[:i-1]中
子序列等于t[:j]的数目；若相等，则s[:i]中子序列等t[:j]的数目的数目应该是s[:i-1]中子序列等于t[:j-1]的子序列数据与
s[:i-1]中子序列等于t[:j]之和。递推公式如下：   
>  1. 如果s[i] == t[j]，则dp[i][j] = dp[i-1][j-1] + dp[i-1][j]   
>  2. 如果s[i] ！= t[j]，则dp[i][j] = dp[i-1][j]

通过观察递推公式可知，dp[i][j]仅和dp[i-1][j]和dp[i-1][j]有关，因此可以用一维数组代替矩阵。   
然后考虑边界条件，如果t为空，则空时任何集合的子集，总数为1。如果s为空，则t不为空时，总数为零。如果将s和t第0位补上""，则
> dp[0][0] = 1   
> dp[0][1:] = 0   
> dp[:][0] = 1   

| |""|r|a|b|b|i|t|
|---|---|---|---|---|---|---|---|
|""|1|0|0|0|0|0|0|
|r|1|1||0|0|0|0|
|a|1|1|1|0|0|0|0|
|b|1|1|1|1|0|0|0|
|b|1|1|1|2|1|0|0|
|b|1|1|1|3|3|0|0|
|i|1|1|1|3|3|3|0|
|t|1|1|1|3|3|3|3|

```python
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for i in range(len(s)):
            before = 1
            for j in range(min(i + 1, len(t))):
                tmp = dp[j + 1]
                if s[i] == t[j]:
                    dp[j + 1] = dp[j + 1] + before
                before = tmp
        return dp[-1]
```