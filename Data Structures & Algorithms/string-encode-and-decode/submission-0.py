class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            lenght = str(len(strs[i]))
            res+=lenght
            res+="#"
            res+=strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            lenght = ""
            while s[i] != "#":
                lenght += s[i]
                i += 1
            i += 1
            k = int(lenght)
            string = s[i:i+k]
            res.append(string)
            i += k
        return res