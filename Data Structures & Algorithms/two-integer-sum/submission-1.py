class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j]
        # return []


        # hashmap
        pos={}
        for i,x in enumerate(nums):
            need=target-x
            if need in pos:
                return[pos[need],i]
            pos[x]=i



        
        