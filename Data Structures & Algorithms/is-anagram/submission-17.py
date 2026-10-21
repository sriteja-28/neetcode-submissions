class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): 
            return False
        
        count=[0]*26 #3
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True

        # countS,countT={},{} #2(using get)
        # for i in range(len(s)):
        #     countS[s[i]]=1+countS.get(s[i],0)
        #     countT[t[i]]=1+countT.get(t[i],0)
        # return countS==countT

        # return Counter(s)==Counter(t)

        # s_count={} #2
        # for char in s:
        #     if char in s_count:
        #         s_count[char]+=1
        #     else:
        #         s_count[char]=1
        
        # t_count={}
        # for char in t:
        #     if char in t_count:
        #         t_count[char]+=1
        #     else:
        #         t_count[char]=1

        # return s_count==t_count

        # return sorted(s)==sorted(t) #1
        