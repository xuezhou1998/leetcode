class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minN=-1
        maxN=-1
        lst=[]
        currD=0
        currL=0
        Lenlst=[]
        maxIdx=-1
        minIdx=-1
        print("begin")
        for i in range(len(nums)):
            print(lst,currL,minN,maxN,minIdx,maxIdx)
            
            if len(lst)==0:
                print("b1")
                lst.append(nums[i])
                minIdx=i
                maxIdx=i
                minN=nums[i]
                maxN=nums[i]
                currD=0
                currL=1
            elif nums[i]>minN and nums[i]<maxN:
                print("b2")
                lst.append(nums[i])
                currL+=1
                # if i==len(nums)-1:
                #     print("b2-1")
                #     Lenlst.append(currL)
            elif nums[i]==minN:
                print("b5")
                lst.append(nums[i])
                currL+=1
                # if i==len(nums)-1:
                #     print("b5-1")
                #     Lenlst.append(currL)
                minIdx=i
            elif nums[i]==maxN:
                print("b5")
                lst.append(nums[i])
                currL+=1
                # if i==len(nums)-1:
                #     print("b5-1")
                #     Lenlst.append(currL)
                maxIdx=i
            elif nums[i]<minN:
                
                if abs(nums[i]-maxN)<=limit:
                    print("b3-1")
                    lst.append(nums[i])
                    currD=abs(nums[i]-maxN)
                    minN=nums[i]
                    minIdx=i
                    currL+=1
                else:
                    print("b3-2")
                    Lenlst.append(currL)
                    cutIdx=maxIdx
                    for j in range(maxIdx,i):
                        if nums[j]==maxN:
                            cutIdx=j
                    lst=nums[cutIdx+1:i]
                    lst.append(nums[i])
                    if len(lst)==1:
                        maxIdx=i
                        maxN=nums[i]
                    else:
                        maxN=max(lst)
                        maxIdx=lst.index(maxN)
                        
                    minN=nums[i]
                    minIdx=i
                    currL=len(lst)
            elif nums[i]>maxN:
                if abs(nums[i]-minN)<=limit:
                    print("b4-1")
                    lst.append(nums[i])
                    currD=abs(nums[i]-minN)
                    maxN=nums[i]
                    maxIdx=i
                    currL+=1
                else:
                    print("b4-2")
                    Lenlst.append(currL)
                    cutIdx=minIdx
                    for j in range(minIdx,i):
                        if nums[j]==minN:
                            cutIdx=j
                    lst=nums[cutIdx+1:i]
                    lst.append(nums[i])
                    if len(lst)==1:
                        minIdx=i
                        minN=nums[i]
                    else:
                        minN=min(lst)
                        minIdx=lst.index(minN)
                    maxN=nums[i]
                    maxIdx=i
                    currL=len(lst)
            if i==len(nums)-1:
                    print("bx-1")
                    Lenlst.append(currL)
            
        print("lenlst",Lenlst)
        if len(Lenlst)==0:
            return 1
        else:
            return max(Lenlst)
                