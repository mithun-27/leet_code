"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 """

#answer

class Solution:
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total

"""Steps Explained:
1. We define a dictionary `values` that maps each Roman numeral character to its corresponding integer value.
2. We initialize a variable `total` to 0, which will hold the final integer value.
3. We iterate through each character in the string `s` using a for loop.
4. For each character, we check if it is followed by a character with a higher value. If it is, we subtract its value from `total` (this handles the subtraction cases like IV, IX, etc.). Otherwise, we add its value to `total`.
5. Finally, we return the computed `total`.

example walkthrough: "LVIII"

Roman numeral = 58.

Start: total = 0

L (50), next = V (5) → 50 > 5 → add → total = 50

V (5), next = I (1) → 5 > 1 → add → total = 55

I (1), next = I (1) → not smaller → add → total = 56

I (1), next = I (1) → not smaller → add → total = 57

I (1), last element → add → total = 58
  
Final Answer = 58




2.example walkthrough: "MCMXCIV"

Roman numeral = 994

Start: total = 0

C (100), next = M (1000) → 100 < 1000 → subtract → total = -100

M (1000), next = X (10) → 1000 > 10 → add → total = 900

X (10), next = C (100) → 10 < 100 → subtract → total = 890

C (100), next = I (1) → 100 > 1 → add → total = 990

I (1), next = V (5) → 1 < 5 → subtract → total = 989

V (5), last element → add → total = 994

Final Answer = 994

"""