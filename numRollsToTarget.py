class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dictNN={}
        def dp(d,f,t):
            if t==0:
                dictNN[(d,f,t)]=0
            elif d==1 and f>=t:
                dictNN[(d,f,t)]=1
            elif d==1 and f<t:
                dictNN[(d,f,t)]=0
            
            else:
                summ=0
                for i in range(1,f+1):
                    if t-i>=0:
                        if (d-1,f,t-i) not in dictNN.keys():
                            dp(d-1,f,t-i)
                            addi=dictNN[(d-1,f,t-i)]
                        else:
                            addi=dictNN[(d-1,f,t-i)]
                        summ+=addi
                dictNN[(d,f,t)]=summ

        dp(d,f,target)
        ret=dictNN[(d,f,target)]
        print(ret)
        
        return ret % (10**9 +7)
