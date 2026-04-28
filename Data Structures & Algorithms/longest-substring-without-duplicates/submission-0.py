class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            lsubstr = ''
            seen = set()

            lsubstr += s[i]
            seen.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] in seen:
                    break
                lsubstr += s[j]
                seen.add(s[j])
            max_len = max(max_len, len(lsubstr))

        return max_len


        