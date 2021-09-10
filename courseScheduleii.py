class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        tk=[]
        pre=set()
        crs=set()
        pq=set()
        tot=set()
        unn=set()
        for i in range(numCourses):
            tot.add(i)
        for i in prerequisites:
            pq.add(tuple(i))
            crs.add(i[0])
            pre.add(i[1])
            unn.add(i[0])
            unn.add(i[1])
        # print(tot,unn)
        tot=tot.difference(unn)
        # print(tot,"tot")
        tk=pre.difference(crs)
        crs.difference(tk)
        cyc=False
        # tk=list(tk)
        
        stk=[]
        
        tk2=[]
        def dfs(h):
            if h not in tk2:
                tk2.append(h)
            for i in crs:
                if (i,h) in pq:
                    if i not in tk2:
                        stem=False
                        for x in pq:
                            if i == x[0]:
                                if x[1] in tk2:
                                    
                                    pass
                                else:
                                    stem=True
                                    break
                        if stem==True:
                            continue
                        else:
                            stk.append(h)
                            dfs(i)
                            stk.pop()
                        
                    elif i in stk:
                        cyc=True
                        return 0
                    else:
                        pass
            return 0
        if tk==set():
            ret= []
        else:
            for i in list(tk):
                dfs(i)
        if cyc==True:
            ret= []
        
            
        else:
            # print(tk,tot)
            if len(tk2)+len(list(tot))<numCourses:
                ret=[]
            else:
                ret=(list(tk2))+list(tot)
        return ret
                    
                        
        
            