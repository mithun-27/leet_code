"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique."""

#answer
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, s, i, j):
        node = self.root
        for idx in range(i, j + 1):
            if s[idx] not in node.children:
                return False
            node = node.children[s[idx]]
        return node.is_word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        t = 0
        for w in wordDict:
            t = max(t, len(w))

        for i in range(len(s), -1, -1):
            for j in range(i, min(len(s), i + t)):
                if trie.search(s, i, j):
                    dp[i] = dp[j + 1]
                    if dp[i]:
                        break

        return dp[0]
    
#example usage
print(Solution().wordBreak("leetcode", ["leet","code"]))  # Output: True    
print(Solution().wordBreak("applepenapple", ["apple","pen"]))  # Output: True
print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # Output: False

"""walkthrough
1. Define a TrieNode class to represent each node in the trie, which contains a dictionary of children and a boolean is_word to indicate if the node represents the end of a word.  
2. Define a Trie class to manage the trie structure, with methods to insert words and search for words in the trie.
3. In the Solution class, create a trie and insert all words from the wordDict into it.
4. Initialize a dynamic programming array dp of size len(s) + 1, where dp[i] indicates whether the substring s[i:] can be segmented into words from the dictionary. Set dp[len(s)] to True since an empty string can be segmented.  
5. Calculate the maximum length of words in the wordDict to optimize the search process.
6. Iterate through the string s from the end to the beginning, and for each index i, check substrings of length up to t (the maximum word length) starting from i. If a substring s[i:j+1] is found in the trie, set dp[i] to dp[j + 1]. If dp[i] becomes True, break out of the inner loop since we found a valid segmentation starting at index i.    
7. Finally, return dp[0] which indicates whether the entire string s can be segmented into words from the dictionary.
8. The time complexity of this algorithm is O(n * m) where n is the length of the string s and m is the maximum length of words in the wordDict. The space complexity is O(n) for the dp array and O(k * l) for the trie, where k is the number of words in the wordDict and l is the average length of those words.
"""