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