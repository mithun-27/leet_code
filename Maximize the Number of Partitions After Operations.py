"""You are given a string s and an integer k.

First, you are allowed to change at most one index in s to another lowercase English letter.

After that, do the following partitioning operation until s is empty:

Choose the longest prefix of s containing at most k distinct characters.
Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

Example 1:

Input: s = "accca", k = 2

Output: 3

Explanation:

The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

Then we perform the operations:

The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
Finally, we remove "a" and s becomes empty, so the procedure ends.
Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:

Input: s = "aabaab", k = 3

Output: 1

Explanation:

Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:

Input: s = "xxyz", k = 1

Output: 4

Explanation:

The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions"""

#answer
from typing import List

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        bit_masks = [1 << (ord(c) - 97) for c in s]

        def build_prefix_info(arr: List[int]):
            prefix_count = [0]
            prefix_mask = [0]
            mask = 0
            groups = 0
            for bit in arr:
                mask |= bit
                if mask.bit_count() > k:
                    groups += 1
                    mask = bit
                prefix_count.append(groups)
                prefix_mask.append(mask)
            return prefix_count, prefix_mask

        prefix_count, prefix_mask = build_prefix_info(bit_masks)
        suffix_count, suffix_mask = build_prefix_info(bit_masks[::-1])

        res = 0
        for i in range(n):
            left_groups = prefix_count[i]
            right_groups = suffix_count[-(i + 2)]
            left_mask = prefix_mask[i]
            right_mask = suffix_mask[-(i + 2)]
            combined_mask = left_mask | right_mask
            left_bits = left_mask.bit_count()
            right_bits = right_mask.bit_count()
            combined_bits = combined_mask.bit_count()

            if min(combined_bits + 1, 26) <= k:
                total = left_groups + right_groups + 1
            elif left_bits == right_bits == k and combined_bits < 26:
                total = left_groups + right_groups + 3
            else:
                total = left_groups + right_groups + 2

            if total > res:
                res = total

        return res
    
#example
s = Solution()
print(s.maxPartitionsAfterOperations("accca", 2)) # Output: 3
print(s.maxPartitionsAfterOperations("aabaab", 3)) # Output: 1
print(s.maxPartitionsAfterOperations("xxyz", 1)) # Output: 4