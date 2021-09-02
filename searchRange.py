class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fd=False
        hd=-1
        tl=-1
        for i in range(len(nums)):
            if nums[i]==target and fd==False:
                hd=i
                tl=i
                fd=True
            elif nums[i]==target:
                tl+=1
            else:
                pass
        if fd==False:
            return [-1,-1]
        else:
            return [hd,tl]
            
