class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums=sorted(nums)
        print(snums)
        numset=set()
        fresult=[]
        for i in range(len(nums)-1):
            if snums[i]>0:
                break
            newnums=snums[i+1:]
            # print(newnums,(-1)*snums[i])
            result=self.twoSum(newnums,(-1)*snums[i])
            
            if result!=[]:
                subresult=[]
                for j in range(len(result)):
                    result[j].append(snums[i])
                    result[j]=sorted(result[j])
                    if tuple(result[j]) not in numset:
                        numset.add(tuple(result[j]))
                        subresult.append(result[j])
                fresult+=subresult
                
        return fresult
    def twoSum(self, nums,twosum):
        retlst=[]
        lo=0
        hi=len(nums)-1
        while lo<hi:
            if nums[lo]+nums[hi]<twosum:
                lo+=1
            elif nums[lo]+nums[hi]>twosum:
                hi-=1
            elif nums[lo]+nums[hi]==twosum:
                
                retlst.append([nums[lo],nums[hi]])
                lo+=1
                hi-=1

        return retlst
    
            