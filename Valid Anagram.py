"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters."""


#answer

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

# Example usage:
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))          # Output: False

"""walkthrough
1. We define a class Solution with a method isAnagram that takes two strings s and t as input.
2. We first check if the lengths of the two strings are different. If they are, we return False immediately, as they cannot be anagrams.
3. We initialize two empty dictionaries, countS and countT, to keep track of the frequency of each character in strings s and t, respectively.
4. We iterate through the indices of the strings using a for loop. For each character in both strings, we update their counts in the respective dictionaries.
5. Finally, we compare the two dictionaries. If they are equal, it means both strings have the same character frequencies, and we return True. Otherwise, we return False.
6. We provide example usage of the Solution class to demonstrate how it works.  
"""