class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in range(len(strs)):
            encoded_string+=strs[i]+"-"
        return encoded_string


    def decode(self, s: str) -> List[str]:
        s=s.split("-")
        s.pop()
        return(s)
