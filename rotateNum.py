class Solution:
    def rotatedDigits(self, n: int) -> int:
        print("begin")
        d={}
        d2={}
        f=1
        for i in range(1,n+1):
            # print(d,d2,i)
            f=max(f,len(str(i)))
            if len(str(i))==1:
                if i in [2,5,6,9]:
                    if f not in d.keys():
                        d[f]=[i]
                    else:
                        d[f].append(i)
                elif i in [0,1,8]:
                    if f not in d2.keys():
                        d2[f]=[i]
                    else:
                        d2[f].append(i)
                else:
                    pass
            else:
                
                la=int(str(i)[:len(str(i))-1])
                if f-1 in d.keys():
                    # print("b1")
                    if la in d[f-1]:
                        # print("b11")
                        if int(str(i)[-1]) in [2,5,6,9,1,0,8]:
                            # print("b111")
                            if f not in d.keys():
                                # print("b1111")
                                d[f]=[i]
                            else:
                                # print("b1112")
                                d[f].append(i)
                        else:
                            pass
                if f-1 in d2.keys():
                    # print("a1")
                    if la in d2[f-1]:
                        # print("a11",str(i)[-1])
                        if int(str(i)[-1]) in [2,5,6,9]:
                            # print("a111")
                            if f not in d.keys():
                                # print("a1111")
                                d[f]=[i]
                            else:
                                # print("a1112")
                                d[f].append(i)
                        elif int(str(i)[-1]) in [0,1,8]:
                            # print("a112")
                            if f not in d2.keys():
                                # print("a1121")
                                d2[f]=[i]
                            else:
                                # print("a1122")
                                d2[f].append(i)
                        
                        else:
                            # print("a113")
                            pass
                    

            
        ret=0
        for i in d.keys():
            ret+=len(d[i])
        return ret
