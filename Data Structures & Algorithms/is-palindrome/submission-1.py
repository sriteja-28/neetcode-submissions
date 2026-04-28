class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().replace(' ','').replace('?','')
        newStr=''
        for ch in s:
            if ch.isalnum():
                newStr+=ch.lower()
        return newStr==newStr[::-1]
        