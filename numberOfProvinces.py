class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ct=isConnected
        pvs=[]
        for i in range(len(ct)):
            for j in range(len(ct[0])):
                
                if ct[i][j]==1:
                    # print(pvs,i,j)
                    iset=None
                    jset=None
                    if pvs!=[]:
                        # print("b1")
                        for k in range(len(pvs)):
                            if pvs[k]!=None:
                                # print("b2")
                                if i in pvs[k]:
                                    iset=k
                                if j in pvs[k]:
                                    jset=k
                        if iset!=None and jset!=None:
                            # print("b3")
                            if iset!=jset:
                                # pvs.remove(iset)
                                # pvs.remove(jset)
                                # pvs.append(iset.union(jset))
                                pvs[iset]=pvs[iset].union(pvs[jset])
                                pvs.remove(pvs[jset])
                            else:
                                pass
                        elif iset!=None:
                            # print("b4")
                            # pvs.remove(iset)
                            # pvs.append(iset.add(j))
                            # print(pvs[iset])
                            pvs[iset].add(j)
                            # pvs[iset]=a
                            
                        elif jset!=None:
                            # print("b5") 
                            # pvs.remove(jset)
                            # pvs.append(jset.add(i))
                            pvs[jset].add(i)
                            # pvs[jset]=a
                        else:
                            # print("b6")
                            pvs.append(set([i,j]))
                    else:
                        # print("b7")
                        pvs.append(set([i,j]))
        return len(pvs)
