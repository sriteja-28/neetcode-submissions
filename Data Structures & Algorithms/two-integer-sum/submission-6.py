class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap={} # hasmap 1 pass
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n]=i

        # indices={} # hasmap 2 pass
        # for i,n in enumerate(nums):
        #     indices[n]=i
        
        # for i,n in enumerate(nums):
        #     diff=target-n
        #     if diff in indices and indices[diff]!=i:
        #         return [i,indices[diff]]
        # return []
        

        # for i in range(len(nums)): #1
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j]
        

        