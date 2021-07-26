
'''
psodou code:

function recrr(s):
    summation=""
    for each item in s:
        summation+=recrr(item)

the key point is to parse each item in the string s, where we employ
a level variable to fetch the items in most outer layer. when we encounter "["
level increases by one, when we encounter "]", level decreases by one.
The level is reset in each recursion, since it is only a representation of the relative inner/outter 
position of each pair of [].
'''
class Solution:
    def decodeString(self, s: str) -> str:
        return self.recrr(s)
    def recrr (self,s:str):
        l=0
        currL=l
        serisLst=[]
        serisFns=True
        contLst=[]
        ret=""
        for i in range(len(s)):
            if s[i].isdigit()==True:
                if currL==l:
                    if serisFns==True:
                        serisLst.append(s[i])
                        serisFns=False
                    else:
                        serisLst[-1]+=s[i]
                        
                else:
                    pass
            elif s[i]=='[':
                serisFns=True
                currL+=1
                if currL==l+1:
                    contLst.append([i+1,-1])
                else:
                    pass
            elif s[i]==']':
                currL-=1
                if currL==l:
                    contLst[-1][1]=i
                    numb=int(serisLst.pop(0))
                    cont=contLst.pop(0)
                    cont=self.recrr(s[cont[0]:cont[1]]) 
                    ret+=numb*cont
                    print(numb,cont)
                else:
                    pass
            elif currL==l:
                ret+=s[i]
        return ret