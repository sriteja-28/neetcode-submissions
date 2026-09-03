class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s)==Counter(t) 
        if len(s)!=len(t):
            return False

        # return sorted(s)==sorted(t)

        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        
        for val in count:
            if val!=0:
                return False
        return True

        # f_s={}
        # f_t={}
        # for item in s:
        #     f_s[item]=f_s.get(item,0)+1

        # for item in t:
        #     f_t[item]=f_t.get(item,0)+1

        # return f_s==f_t
             