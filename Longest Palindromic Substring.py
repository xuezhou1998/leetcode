class Solution:
    def longestPalindrome(self, s: str) -> str:
        divider=0
        maxP=1
        pal=[]
        result=s[0]
        if len(s)==1:
            return result
        while divider<len(s):
            indx=1
            

            locmaxP=1
            
            while True:
                if divider-indx<0 or divider+indx>=len(s):
                    if locmaxP>maxP:
                        result=locres
                        maxP=locmaxP
                    break
                elif s[divider-indx]==s[divider+indx]:
                    locmaxP+=2
                    
                    locres=s[divider-indx:divider+indx+1]
                    indx+=1
                else:
                    if locmaxP>maxP:
                        result=locres
                        maxP=locmaxP
                    break
            locmaxP=0
            indx=1
            while True:
                if divider-(indx-1)<0 or divider+indx>=len(s):
                    if locmaxP>maxP:
                        result=locres
                        maxP=locmaxP
                    break
                elif s[divider-(indx-1)]==s[divider+indx]:
                    locmaxP+=2
                    locres=s[divider-(indx-1):divider+indx+1]
                    indx+=1
                else:
                    if locmaxP>maxP:
                        result=locres
                        maxP=locmaxP
                    break
            divider+=1
        return result

