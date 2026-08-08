class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs[0])):

            ele = strs[0][i]

            for string in strs:
                if i >= len(string):
                    return s

                if string[i]!=ele:
                    return s
            
            s += ele

        return s
                
            
        