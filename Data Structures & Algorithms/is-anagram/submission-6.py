class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s)==Counter(t)
        # if len(s) != len(t):
        #     return False

        # return sorted(s) == sorted(t)

        sC={}
        tC={}
        for i in s:
            sC[i]=sC.get(i, 0) + 1

        for j in t:
            tC[j]=tC.get(j, 0) + 1
            
        return sC==tC



        