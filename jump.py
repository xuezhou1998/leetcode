class Solution:
    def jump(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            d[i]=999999999
        
        n=nums.copy()
        
        idx=0
        a=n.pop(idx)
        d[idx]=0
        
        while len(n)>0:
            for i in range(a):
                if idx+1+i<len(nums):
                    
                    if d[idx]+1<d[idx+1+i]:
                        d[idx+1+i]=d[idx]+1
                    else:
                        pass
                else:
                    return d[len(nums)-1]
                    
            a=n.pop(0)
            idx+=1
            
        return d[len(nums)-1] 
                
