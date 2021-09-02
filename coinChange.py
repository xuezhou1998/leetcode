class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        d={}
        # for i in coins:
        #     d[i]=1
        def rec(am):
            # print(am,d)
            if am<0:
                return -1
            elif am==0:
                return 0
            elif am in coins:
                d[am]=1
                return 1
            maxn=-1
            res=None
            for i in coins:
                if am-i in d.keys():
                    if d[am-i]==-1:
                        continue
                    else:
                        res=d[am-i]+1
                else:
                    
                    if rec(am-i)==-1:
                        continue
                    else:
                        res=rec(am-i)+1
                if res!=None:
                    if maxn==-1:
                        maxn=res
                    else:
                        maxn=min(maxn,res)
            if res==None:
                d[am]=-1
                return -1
            else:
                d[am]=maxn
                return maxn
        return rec(amount)
        
        
        # return d[amount]
            
