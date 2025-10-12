"""You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned."""

#answer

from bisect import bisect_left

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        m = len(potions)
        ans = []
        
        for spell in spells:
            min_potion = (success + spell - 1) // spell
            idx = bisect_left(potions, min_potion)
            ans.append(m - idx)  
        
        return ans    

#example
solution = Solution()
print(solution.successfulPairs([5,1,3], [1,2,3,4,5], 7))  # Output: [4,0,3]
print(solution.successfulPairs([3,1,2], [8,5,8], 16))  # Output: [2,0,2]
print(solution.successfulPairs([10,20,30], [1,2,3,4,5], 100))  # Output: [0,0,1]


"""walkthrough
1. Import the bisect_left function from the bisect module to perform binary search.
2. Define the Solution class with the successfulPairs method that takes spells, potions, and success as input.
3. Sort the potions array to enable binary search.
4. Initialize an empty list ans to store the results.
5. Iterate through each spell in the spells array:
   a. Calculate the minimum potion strength required to form a successful pair with the current spell using the formula (success + spell - 1) // spell. This ensures we round up to the nearest integer.
   b. Use bisect_left to find the index of the first potion in the sorted potions array that is greater than or equal to min_potion.
   c. The number of successful pairs for the current spell is the total number of potions minus the index found in step 5b. Append this value to ans.
6. Return the ans list containing the number of successful pairs for each spell.
7. Test the implementation with example cases to ensure correctness."""