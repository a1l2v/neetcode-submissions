class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = Counter(s1)
        seen = Counter(s2[:len(s1)])

        if dict_s1 == seen:
            return True
        for right in range(len(s1),len(s2)):

            seen[s2[right-len(s1)]] -= 1
            if seen[s2[right-len(s1)]] == 0:
                del seen[s2[right-len(s1)]]
            seen[s2[right]] = seen.get(s2[right],0) + 1

            if seen == dict_s1:
                return True
        return False