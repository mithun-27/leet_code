"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""

#answer:

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix    
    
j = Solution()
print(j.longestCommonPrefix(["flower","flow","flight"]))
print(j.longestCommonPrefix(["dog","racecar","car"]))


"""walkthrough:
1. We define a class `Solution` with a method `longestCommonPrefix` that takes a list of strings `strs`.
2. We first check if the input list `strs` is empty. If it is, we return an empty string.
3. We initialize a variable `prefix` with the first string in the list.
4. We then iterate through the remaining strings in the list.
5. For each string, we check if it starts with the current `prefix`. If not, we shorten the `prefix` by removing the last character.
6. If at any point the `prefix` becomes empty, we return an empty string.
7. If we finish checking all strings, we return the longest common prefix found."""