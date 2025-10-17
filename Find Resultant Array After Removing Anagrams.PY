"""You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

 

Example 1:

Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.
Example 2:

Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed."""

#answer

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def freq(s):
            ans=0
            for c in s:
                i=ord(c)-97
                ans+=(1<<4*i)
            return ans
        n, l=len(words), 0
        ans=[words[0]]
        f0=freq(words[0])
        for r in range(1, n):
            s=words[r]
            x=freq(s)
            if f0!=x:
                ans.append(s)
                l=r
                f0=x
        return ans

#example
s = Solution()
print(s.removeAnagrams(["abba","baba","bbaa","cd","cd"])) # Output: ["abba","cd"]
print(s.removeAnagrams(["a","b","c","d","e"])) # Output: ["a","b","c","d","e"]  

"""walkthrough
1. The function removeAnagrams is defined within the Solution class.
2. It takes a single parameter words, which is a list of strings.
3. A helper function freq is defined to calculate a unique frequency representation of each word using bit manipulation.
4. The main logic iterates through the words list, comparing the frequency representation of each word with the previous one.
5. If the current word is not an anagram of the previous one, it is added to the result list ans.
"""

