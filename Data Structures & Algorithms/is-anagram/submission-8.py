class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s)==Counter(t) 

        f_s={}
        f_t={}
        for item in s:
            f_s[item]=f_s.get(item,0)+1

        for item in t:
            f_t[item]=f_t.get(item,0)+1

        return f_s==f_t
             