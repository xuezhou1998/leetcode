class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        hd=0
        tl=len(nums)-1
        if len(nums)==1:
            return 0
        while True:
            # break
            mid=(hd+tl)//2
            if mid==hd:
                return nums.index(max(nums[hd],nums[tl]))
            elif mid==len(nums)-1:
                return len(nums)-1
            elif nums[mid-1]<nums[mid]<nums[mid+1]:
                hd=mid
            elif nums[mid-1]>nums[mid]>nums[mid+1]:
                tl=mid-1
            elif nums[mid-1]>nums[mid] and nums[mid+1]>nums[mid]:
                hd=mid
            else:
                return mid
        return 0
