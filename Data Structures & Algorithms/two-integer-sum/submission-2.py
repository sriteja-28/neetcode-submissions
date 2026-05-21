class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos={}
        for i,x in enumerate(nums):
            need=target-x
            if need in pos:
                return[pos[need],i]
            pos[x]=i

        