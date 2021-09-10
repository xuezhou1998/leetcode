class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        dd={}
        
        
        for i in nums:
            if len(dd.keys())>=k:
                
                if i in dd.keys():
                    d[i]+=1
                    dd[i]=d[i]
                elif i in d.keys():
                    d[i]+=1
                    minv=min(dd.values())
                    if d[i]>minv:
                        
                        idx=list(dd.values()).index(minv)
                        mink=list(dd.keys())[idx]
                        dd.pop(mink)
                        dd[i]=d[i]
                    
                    
                else:
                    d[i]=1
            else:
                if i in d.keys():
                    d[i]+=1
                    dd[i]=d[i]
                else:
                    d[i]=1
                    dd[i]=d[i]
            # print(dd.get)
        return dd.keys()
                    