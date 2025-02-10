from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        freqs = sorted([(num, c) for num, c in count.items()], key=lambda x:x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(freqs[i][0])

        return res