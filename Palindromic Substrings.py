"""Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters."""

#answer
class Solution:
    def countSubstrings(self, s: str) -> int:

        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manacher(s)
        res = 0
        for i in p:
            res += (i + 1) // 2
        return res
    
#example usage
print(Solution().countSubstrings("abc"))  # Example call to the function
print(Solution().countSubstrings("aaa"))  # Example call to the function
# Output: 3
# Output: 6

"""walkthrough
1. We define a class Solution with a method countSubstrings that takes a string s as input. 
2. Inside the method, we define a helper function manacher that implements Manacher's algorithm to find the lengths of palindromic substrings centered at each character in a transformed string.   
3. The transformed string t is created by inserting '#' characters between each character of s and at the beginning and end. This helps to handle even-length palindromes uniformly.    
4. We initialize an array p to store the lengths of palindromic substrings and two pointers l and r to keep track of the rightmost palindrome found so far. 
5. We iterate through each character in the transformed string t, updating the lengths of palindromic substrings in p using previously computed values and expanding around the center as needed.   
6. After computing the array p, we iterate through it and for each value i, we add (i + 1) // 2 to the result. This is because each palindrome of length i contributes (i + 1) // 2 palindromic substrings to the count.    
7. Finally, we return the total count of palindromic substrings.
"""