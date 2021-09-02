class Solution:
    def maxSumTwoNoOverlap(self, nums: list, firstLen: int, secondLen: int) -> int:
        # firstLst=nums[:len(firstLen)]
        # secondLst=nums[len(firstLen):len(secondLen)]
        # while True:
        #     pass
        largeLen=max(firstLen,secondLen)
        smallLen=min(firstLen,secondLen)
        retMax=-1
        for i in range(len(nums)):
            currLst=nums[i:i+largeLen]
            mySubSum=self.subMaxSum(firstLastIdx=i+largeLen,nums=nums,largeLen=largeLen,smallLen=smallLen)
            retMax=max(retMax,mySubSum+sum(currLst))

            # print(i,currLst,mySubSum,retMax)
            if i+largeLen == len(nums):
                break
        return retMax
    def subMaxSum(self,firstLastIdx:int,nums:list,largeLen: int, smallLen: int):
        
        # firstLastIdx+=1
        l_avail=nums[:firstLastIdx-largeLen]
        r_avail=nums[firstLastIdx:]
        l_max=0
        r_max=0
        if len(l_avail)>=smallLen:
            l_max=self.slideMax(largeLst=l_avail,smallLen=smallLen)
        if len(r_avail)>=smallLen:
            r_max=self.slideMax(largeLst=r_avail,smallLen=smallLen)
        return max(l_max,r_max)

    def slideMax(self, largeLst:list, smallLen:list):
        retMax=0
        for i in range(len(largeLst)):
            currSmall=largeLst[i:i+smallLen]
            retMax=max(retMax,sum(currSmall))
            if i+smallLen == len(largeLst):
                break
        return retMax