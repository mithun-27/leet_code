"""You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

Potion Number	Start time	Wizard 0 done by	Wizard 1 done by	Wizard 2 done by	Wizard 3 done by
0	0	5	30	40	60
1	52	53	58	60	64
2	54	58	78	86	102
3	86	88	98	102	110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21"""

#answer

class Solution:
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n = len(skill)
        m = len(mana)

        total_skill = sum(skill)
        prev_wizard_done = total_skill * mana[0]

        for j in range(1, m):
            prev_potion_done = prev_wizard_done

            for i in range(n - 2, -1, -1):
                prev_potion_done -= skill[i + 1] * mana[j - 1]
                candidate = prev_wizard_done - skill[i] * mana[j]

                if prev_potion_done > candidate:
                    prev_wizard_done = prev_potion_done
                else:
                    prev_wizard_done = candidate

            prev_wizard_done += total_skill * mana[j]

        return prev_wizard_done
    
#example
s = Solution()
print(s.minTime([1,5,2,4], [5,1,4,2]))
# Output: 110
print(s.minTime([1,1,1], [1,1,1]))
# Output: 5
print(s.minTime([1,2,3,4], [1,2]))
# Output: 21



"""walkthrough:
We can use dynamic programming to solve this problem. The idea is to keep track of the minimum time required to complete the brewing process for each potion and each wizard.
1. Initialize variables:
   - n: Number of wizards.
   - m: Number of potions.
   - total_skill: Sum of all skill levels of the wizards.
   - prev_wizard_done: Time when the previous wizard finished the first potion.
2. Loop through each potion (from the second to the last):
    - Set prev_potion_done to the time when the previous wizard finished the last potion.
    - Loop through each wizard (from the second last to the first):
      - Update prev_potion_done by subtracting the time taken by the next wizard for the previous potion.
      - Calculate candidate time for the current wizard and potion.
      - Update prev_wizard_done to be the maximum of prev_wizard_done and candidate.
    - After processing all wizards for the current potion, add the total skill multiplied by the current potion's mana to prev_wizard_done.
3. Return prev_wizard_done, which contains the minimum time required to brew all potions.
"""