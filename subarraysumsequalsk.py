class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d={}     
        cts=0
        d[0]=1
        sms=0
        for i in nums:
            sms+=i
            
            cts+=d.get(sms-k,0)
            d[sms]=d.get(sms,0)+1
        return cts
            
        
                