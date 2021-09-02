class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(self.sm(nums))
        idx=self.sm(nums)
        if target>=nums[idx] and target<=nums[len(nums)-1]:
            res=self.bs(nums[idx:],target)
            if res>=0:
                
                return idx+res
            else:
                return -1
        else:
            res=self.bs(nums[:idx],target)
            if res>=0:
                return res
            else:
                
                return -1 
        return 0
    def bs(self,nums:List[int],t:int)->int:
        if nums==[]:
            return -1
        l=0
        r=len(nums)-1
        while True:
            mid=(l+r)//2
            if r==l:
                if nums[l]==t:
                    
                    return l
                else:
                    return -1
            elif r-l==1:
                if nums[l]==t:
                    return l
                elif nums[r]==t:
                    return r
                else:
                    return -1
            elif t>=nums[mid]:
                l=mid
            else:
                r=mid-1
                
        return 0
    def sm(self,nums:List[int])->int:
        if len(nums)==1:
            return 0
        
        mid=len(nums)//2-1
        lf=0
        rt=len(nums)-1
        while True:
            mid=(lf+rt)//2
            if abs(lf-rt)==1:
                if nums[lf]<nums[rt]:
                    return lf
                else:
                    return rt
            elif abs(lf-rt)==2:
                piv=min(nums[lf:rt+1])
                idx=nums[lf:rt+1].index(piv)
                return lf+idx
            elif nums[lf]>nums[mid]:
                rt=mid
            elif nums[mid]>nums[len(nums)-1]:
                lf=mid
            else:
                return 0
            
