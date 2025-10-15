"""In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.

You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.

In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.

You are given an array energy and an integer k. Return the maximum possible energy you can gain.

Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.

 

Example 1:

Input: energy = [5,2,-10,-5,1], k = 3

Output: 3

Explanation: We can gain a total energy of 3 by starting from magician 1 absorbing 2 + 1 = 3.

Example 2:

Input: energy = [-2,-3,-1], k = 2

Output: -1

Explanation: We can gain a total energy of -1 by starting from magician 2.

"""


#answer

class Solution:
    def maximumEnergy(self, energy, k):
        n = len(energy)
        dp = [0] * n
        ans = float('-inf')

        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
            ans = max(ans, dp[i])
        
        return ans
    

#example
s = Solution()
print(s.maximumEnergy([5,2,-10,-5,1], 3))
# Output: 3
print(s.maximumEnergy([-2,-3,-1], 2))
# Output: -1
print(s.maximumEnergy([1,-2,3,-4,5,-6,7,-8,9], 2))
# Output: 16


"""walkthrough:
You can solve this problem using dynamic programming. The idea is to iterate through the magicians from the end to the beginning, calculating the maximum energy that can be obtained starting from each magician.
You can use a dp array where dp[i] represents the maximum energy that can be obtained starting from magician i. For each magician, you can either take the energy from that magician and jump k steps ahead or just take the energy from that magician if jumping k steps ahead goes out of bounds. Finally, you return the maximum value from the dp array."""