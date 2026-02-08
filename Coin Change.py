"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,721,105/5.7M
Acceptance Rate
47.9%
Topics"""

#answer
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1   

#example usage
solution = Solution()
print(solution.coinChange([1,2,5], 11)) # Output: 3
print(solution.coinChange([2], 3)) # Output: -1
print(solution.coinChange([1], 0)) # Output: 0

"""walkthrough
1. We start by checking if the amount is 0. If it is, we can return 0 immediately since no coins are needed to make up the amount.
2. We initialize a queue (q) to perform a breadth-first search (BFS) and a list (seen) to keep track of the amounts we have already visited. We mark the starting point (0) as seen.
3. We initialize a variable (res) to keep track of the number of coins used.
4. We enter a while loop that continues until the queue is empty. Inside the loop, we increment the res variable to represent the number of coins used in the current level of BFS.
5. We iterate through the current level of the queue, popping each amount (cur) from the queue. For each amount, we iterate through the list of coins and calculate the next amount (nxt) by adding the coin value to the current amount.
6. If the next amount (nxt) is equal to the target amount, we return the current number of coins (res) as the result.
7. If the next amount exceeds the target amount or has already been seen, we skip it. Otherwise, we mark it as seen and add it to the queue for further exploration.
8. If we exhaust the queue without finding the target amount, we return -1 to indicate that it is not possible to make up the amount with the given coins.      
"""