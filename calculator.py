class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        # print("start",s)
        ret,s=self.gt(s)
        while len(s)>0:
            # print(s,"main")
            op=s[0]
            if op=="+" or op=='-':
                res,s=self.gt(s[1:])
                ret=self.op(op,ret,res)
            
        return ret
            
    def gt(self,s:str):
        
        n,l,s=self.gn(s)
        ret=n
        while len(s)>0:
            # print(s,"gt",s[1:])
            op=s[0]
            if op=='+' or op =='-':
                break
            n,l,s=self.gn(s[1:])
            ret=self.op(op, ret, n)
        # print(ret,s)
        return ret,s
        
    def op(self,op:str,m:int,n:int):
        if op=='+':
            return m + n
        if op=='-':
            return m - n
        if op=='*':
            return m * n
        if op=='/':
            return m // n
        
    def gn(self,s:str):
        ans=""
        for i in range(len(s)):
            # print(s,"gn")
            if s[i].isdigit()==True:
                ans+=s[i]
            else:
                return int(ans), len(ans),s[len(ans):]
        return int(ans), len(ans),s[len(ans):]
            
            
