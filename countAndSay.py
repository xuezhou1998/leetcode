class Solution:
    def countAndSay(self, n: int) -> str:
        bas="1"
        for i in range(n):
            if i==0:
                continue
            newbas=""
            retd=self.cdf(bas)
            for i in range(len(retd)):
                newbas+=str(retd[i][1])+str(retd[i][0])
            bas=newbas
        return bas
    def cdf(self, s:str)->dict:
        ret=[]
        pr=-1
        for i in range(len(s)):
            if i ==0:
                ret.append([s[i],1])
                pr=s[i]
            else:
                if s[i]==pr:
                    ret[len(ret)-1][1]=ret[len(ret)-1][1]+1
                else:
                    ret.append([s[i],1])
                    pr=s[i]
        return ret
