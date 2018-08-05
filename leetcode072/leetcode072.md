# 72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

**Example 1:**

> **Input**: word1 = "horse", word2 = "ros"
> **Output**: 3
> **Explanation**:
> horse -> rorse (replace 'h' with 'r')
> rorse -> rose (remove 'r')
> rose -> ros (remove 'e')

**Example 2:**

> **Input**: word1 = "intention", word2 = "execution"
> **Output**: 5
> **Explanation**:
> intention -> inention (remove 't')
> inention -> enention (replace 'i' with 'e')
> enention -> exention (replace 'n' with 'x')
> exention -> exection (replace 'n' with 'c')
> exection -> execution (insert 'u')

题目大意是求一个字符串变成另一个字符串需要的最少操作数，一共有删除一个字符、插入一个字符和替换一个字符3中操作。
这种题目一般通过动态规划来求解。假设dp[i][j]表示word1[:i]到word[:j]需要的最少操作次数。求dp[i+1][j+1]时，
有三种可能：
1. word1[:i]通过dp[i][j+1]次操作变成word2[:j+1]，删除word1[i+1]
2. word1[:i+1]通过dp[i+1][j-1]次操作变成word2[:j]，插入word2[j+1]
3. word1[:i]通过dp[i][j]次操作变成word2[:j]，此时:
    * 如果word1[i+1]==word2[j+1]，则不做任何操作;
    * 否则用word2[j+1]替换word1[i+1]

通过以上分析可以得到以下递推公式：
dp[i+1][j+1] = min(min(dp[i+1,j],dp[i][j+1]) +1),dp[i][j]+ (0 if word1[i+1]==word2[j+1] else 1))


```python
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[i] * (len(word2) + 1) for i in range(len(word1) + 1)]
        dp[0][:] = range(len(word2) + 1)


        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                dp[i][j] = dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)

                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        return dp[-1][-1]
```