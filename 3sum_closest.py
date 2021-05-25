class Solution:
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        summ=0
        for i in range(len(nums)):
            summ+=abs(nums[i])
            
        nums=sorted(nums)
        maxdif=summ+abs(target)
        dif= maxdif
        ret=None
        for i in range(len(nums)-2):
            target2=target-nums[i]
            res=self.twoSumClosest(nums[i+1:], target2, maxdif)
            if abs(res+nums[i]-target)<=abs(dif):
                ret=res+nums[i]
                dif=abs(res+nums[i]-target)
        return ret
                
            
    def twoSumClosest(self, nums, target , maxdif):
        
        lo=0
        hi=len(nums)-1
        dif=maxdif
        ret=None
        while lo<hi:
            if abs((nums[lo]+nums[hi])-target)<=abs(dif):
                dif=(nums[lo]+nums[hi])-target
                
                ret=nums[lo]+nums[hi]
                if (nums[lo]+nums[hi])-target<0:
                    lo+=1
                elif (nums[lo]+nums[hi])-target>0:
                    hi-=1
                else:
                    break
            else:
                if (nums[lo]+nums[hi])-target<0:
                    lo+=1
                elif (nums[lo]+nums[hi])-target>0:
                    hi-=1
                else:
                    ret=nums[lo]+nums[hi]
                    break
        return ret