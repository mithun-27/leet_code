"""Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters."""

#answer
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            prev = 0
            for j in range(len(text2) - 1, -1, -1):
                temp = dp[j]
                if text1[i] == text2[j]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp

        return dp[0]
    
#example usage
solution = Solution()   
print(solution.longestCommonSubsequence("abcde", "ace"))  # Output: 3
print(solution.longestCommonSubsequence("abc", "abc"))  # Output: 3
print(solution.longestCommonSubsequence("abc", "def"))  # Output: 0 

"""walkthrough
1. The function longestCommonSubsequence takes two strings text1 and text2 as input.
2. If the length of text1 is less than the length of text2, we swap them to ensure that text1 is always the longer string. This is done to optimize the space complexity of the algorithm.
3. We initialize a list dp of size len(text2) + 1 with all elements set to 0. This list will be used to store the lengths of the longest common subsequences for different substrings of text2. The extra element at the end is used to handle the case when we are comparing with an empty substring of text2. 
4. We use a nested loop to iterate through the characters of text1 and text2 in reverse order. The outer loop iterates through text1 from the last character to the first, and the inner loop iterates through text2 from the last character to the first.      
5. Inside the inner loop, we store the current value of dp[j] in a temporary variable temp before updating it. This is because we need to use the previous value of dp[j] (which represents the longest common subsequence length for the substring of text2 starting from index j) when calculating the new value of dp[j].    
6. If the characters text1[i] and text2[j] are the same, it means we can extend the longest common subsequence found so far by 1, so we set dp[j] to 1 + prev (where prev is the value of dp[j + 1] from the previous iteration of the inner loop). 
7. If the characters are different, we take the maximum of dp[j] and dp[j + 1] to determine the longest common subsequence length for the current substrings of text1 and text2.    
8. After the inner loop, we update prev to temp to prepare for the next iteration of the outer loop.    
9. After the outer loop completes, dp[0] will contain the length of the longest common subsequence for the entire strings text1 and text2, which we return as the result.   
10. The time complexity of this algorithm is O(m * n), where m and n are the lengths of text1 and text2, respectively, due to the nested loops. The space complexity is O(n) since we are using a single list dp of size len(text2) + 1 to store the intermediate results.
"""