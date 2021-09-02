class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # print('start')
        def cnt(a:str):
            # one=0
            # zero=0
            # for i in a:
            #     if i=='1':
            #         one+=1
            #     else:
            #         zero+=1
            zeros=a.count('0')
            ones=len(a)-zeros
            return (zeros,ones)
        d={}
        
        # for i in range(m+1):
        #     for j in range(n+1):
        #         if (i,j) not in d.keys():
        #             d[(i,j)]=0
        for i in range(len(strs)):
            # print(d)
            p=cnt(strs[i])
            if p[0]<=m and p[1]<=n:
                # if (p[0],p[1]) not in d.keys():
                #     d[(p[0],p[1])]=0
                for j in reversed(range(p[0],m+1)):
                    for k in reversed(range(p[1],n+1)):
                        # a=d[(j,k)]
                        # print(j,k)
                        if (j,k) not in d.keys():
                            d[(j,k)]=0
                        if (j-p[0],k-p[1]) not in d.keys():
                            d[(j-p[0],k-p[1])]=0
                        d[(j,k)]=max(d[(j,k)],1+d[(j-p[0],k-p[1])])
        if d=={}:
            return 0
        return max(d.values())
        
        
                
        