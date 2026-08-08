class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char)-ord('a')] += 1
            
            freq = tuple(freq)
            if freq not in dict:
                dict[freq] = []  

            dict[freq].append(string)

        return list(dict.values())
