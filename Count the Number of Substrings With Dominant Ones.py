"""You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2
Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
 

Constraints:

1 <= s.length <= 4 * 104
s consists only of characters '0' and '1'."""

#answer

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        pref = [0] * (n + 1)
        for i, ch in enumerate(s):
            pref[i+1] = pref[i] + (ch == '1')

        Z = [i for i, ch in enumerate(s) if ch == '0']
        m = len(Z)

        ans = 0

        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            j = i
            while j < n and s[j] == '1':
                j += 1
            L = j - i
            ans += L * (L + 1) // 2
            i = j

        B = isqrt(n) + 2

        def ones(l, r):
            return pref[r+1] - pref[l]

        for a in range(m):
            Lmin = 0 if a == 0 else Z[a-1] + 1
            Lmax = Z[a]
            if Lmin > Lmax:
                continue

            for z in range(1, B + 1):
                b = a + z - 1
                if b >= m:
                    break

                Rmin = Z[b]
                Rmax = Z[b + 1] - 1 if b + 1 < m else n - 1
                if Rmin > Rmax:
                    continue

                need = z * z
                r = Rmin

                for l in range(Lmin, Lmax + 1):
                    if pref[Rmax + 1] - pref[l] < need:
                        continue
                    while r <= Rmax and ones(l, r) < need:
                        r += 1
                    if r > Rmax:
                        break
                    ans += (Rmax - r + 1)

        return ans
    
#sample usage
Solution().numberOfSubstrings("00011")  # Expected output: 5
Solution().numberOfSubstrings("101101")  # Expected output: 16
Solution().numberOfSubstrings("1")  # Expected output: 1

"""walkthrough
1. We define a class Solution with a method numberOfSubstrings that takes a binary string s as input.
2. We calculate the length of the string n.
3. We create a prefix sum array pref to count the number of ones up to each index in the string.
4. We create a list Z to store the indices of zeros in the string.  
5. We initialize a variable ans to store the count of substrings with dominant ones.
6. We iterate through the string to count substrings consisting entirely of ones and add their counts to ans.
7. We define a variable B as the integer square root of n plus 2 to limit the number of zeros we consider.
8. We define a helper function ones(l, r) to calculate the number of ones in the substring s[l..r].
9. We iterate through each zero in Z and for each zero, we consider substrings that contain a certain number of zeros (up to B).
10. For each valid substring defined by the zeros, we calculate the minimum and maximum indices for the left and right boundaries.11. We check if the number of ones in the substring is greater than or equal to the square of the number of zeros and update ans accordingly.
12. Finally, we return the total count of substrings with dominant ones stored in ans.
"""