class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # return (Counter(s)==Counter(t)) 

        # return sorted(s)==sorted(t)    

        s_f={}
        for char in s:
            if char in s_f:
                s_f[char]+=1
            else:
                s_f[char]=1

        t_f={}
        for char in t:
            if char in t_f:
                t_f[char]+=1
            else:
                t_f[char]=1
        return s_f==t_f
        