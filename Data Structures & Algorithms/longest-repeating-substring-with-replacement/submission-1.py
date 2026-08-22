class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      left = 0
      seen = {}
      max_freq = 0
      max_len = 0

      for right in range(len(s)):
        seen[s[right]] = seen.get(s[right],0) + 1
        if seen[s[right]] > max_freq:
          max_freq = seen[s[right]]
        while((right-left+1) - max_freq > k):
          seen[s[left]] -= 1
          left += 1

        max_len = max(max_len,right-left+1)
      return max_len