"""A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6."""

#answer

from typing import List
from collections import Counter
from bisect import bisect_left

class Solution:
    def maximumTotalDamage(self, power: List[int]):
       
        count = Counter(power)
        values = sorted(count.keys())
        total = [v * count[v] for v in values]

        n = len(values)
        if n == 0:
            return 0

        dp = [0] * n

        def find_previous_index(target):
            index = bisect_left(values, target)
            return index - 1

        dp[0] = total[0]
        for i in range(1, n):
            option1 = dp[i - 1]
            j = find_previous_index(values[i] - 2)
            add = dp[j] if j >= 0 else 0
            option2 = total[i] + add
            dp[i] = max(option1, option2)

        return dp[-1]
    
#example
s = Solution()
print(s.maximumTotalDamage([1,1,3,4]))
# Output: 6
print(s.maximumTotalDamage([7,1,6,6]))
# Output: 13
print(s.maximumTotalDamage([2,2,3,3,4,4,5,5,6,6]))
# Output: 18

"""walkthrough:
To solve this problem, we can use dynamic programming. The idea is to first count the total damage for each unique spell damage value, and then use a DP array to keep track of the maximum damage we can achieve up to each unique damage value while adhering to the casting rules.
We can use a Counter to count the occurrences of each spell damage value, and then create a sorted list of unique damage values. For each unique damage value, we have two options: either we skip it and take the maximum damage up to the previous value, or we take it and add its total damage to the maximum damage we can achieve from the last non-conflicting damage value (which is the largest damage value that is at least 2 less than the current one). We can use binary search to efficiently find this last non-conflicting index.
Finally, we return the maximum damage we can achieve up to the last unique damage value.
Context: Path: Taking%20Maximum%20Energy%20From%20the%20Mystic%20Dungeon.py
You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.
In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.
You are given an array energy and an integer k. Return the maximum possible energy you can gain
Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.
Example 1:
Input: energy = [1,2,3,4,5], k = 2
Output: 12
Explanation: You can start at magician 0, absorb 1 energy, teleport to magician 2, absorb 3 energy, teleport to magician 4, absorb 5 energy. The total energy gained is 1 + 3 + 5 = 9.
Example 2:
Input: energy = [5,4,3,2,1], k = 1
Output: 15
Explanation: You can start at magician 0, absorb 5 energy, teleport to magician 1, absorb 4 energy, teleport to magician 2, absorb 3 energy, teleport to magician 3, absorb 2 energy, teleport to magician 4, absorb 1 energy. The total energy gained is 5 + 4 + 3 + 2 + 1 = 15.
"""