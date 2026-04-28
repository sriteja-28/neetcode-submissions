class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            max_len = max(max_len, len(seen))

        return max_len


        