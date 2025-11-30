"""We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
 

Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.
"""

#answer

from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:  # parse until the last bit (we stop before last index)
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        # If we stop exactly at last index, that last bit is a 1-bit character
        return i == n - 1

#sample usage
sol = Solution()
print(sol.isOneBitCharacter([1,0,0]))  # Output: True
print(sol.isOneBitCharacter([1,1,1,0]))  # Output: False
print(sol.isOneBitCharacter([0]))  # Output: True

"""walkthrough
1. Initialize an index `i` to 0 and get the length `n` of the `bits` array.
2. Use a while loop to iterate through the array until `i` is less than `n - 1` (we stop before the last index).
3. Inside the loop, check the value of `bits[i]`:
   - If it is 1, increment `i` by 2 (since it's a two-bit character).
   - If it is 0, increment `i` by 1 (since it's a one-bit character).
4. After the loop, check if `i` is equal to `n - 1`. If it is, it means we stopped exactly at the last index, indicating that the last character is a one-bit character. Return `True` in this case; otherwise, return `False`.
5. This approach efficiently parses the array in a single pass, determining the nature of the last character based on the parsing rules.
"""