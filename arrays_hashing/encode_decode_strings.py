class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            temp = str(len(s)) + "#" + s
            res += temp
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        nums = [str(i) for i in range(10)]
        while s:
            ni = 1
            while s[ni] in nums:
                ni += 1
            length = int(s[:ni])
            s = s[ni+1:]
            res.append(s[:length])
            s = s[length:]
        return res
