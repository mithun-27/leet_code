"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters."""

#answer
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Example usage:
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""]))  # Output: [[""]]   
print(solution.groupAnagrams(["a"]))  # Output: [["a"]]


"""walkthrough
1. We define a class Solution with a method groupAnagrams that takes a list of strings strs as input.
2. We initialize a defaultdict res to store lists of anagrams, where the keys will be tuples representing character counts.
3. We iterate through each string s in the input list strs.
4. For each string s, we create a list count of size 26 initialized to zero, representing the count of each letter in the English alphabet.
5. We iterate through each character c in the string s and update the count list by incrementing the count at the index corresponding to the character c.
6. We convert the count list to a tuple (to make it hashable) and use it as a key in the res dictionary, appending the string s to the list of anagrams for that key.
7. Finally, we return the values of the res dictionary as a list of lists, which contains the grouped anagrams.
"""