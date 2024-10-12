from typing import List
import collections


class Solution:
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)

        most_common = counter.most_common(k)

        result = [item[0] for item in most_common]

        return result

# Solution by neetcode
# def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#     count = {}
#     freq = [[] for i in range(len(nums) + 1 )]
#
#     for n in nums:
#         count[n] = 1 + count.get(n, 0)
#     for n, c in count.items():
#         freq[c].append(n)
#
#     res = []
#     for i in range(len(freq) - 1, 0, -1):
#         for n in freq[i]:
#             res.append(n)
#             if len(res) == k:
#                 return res