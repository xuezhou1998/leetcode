import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ptdict={}
        for i in range(len(points)):
            dist=math.sqrt(points[i][0]**2+points[i][1]**2)
            ptdict[tuple(points[i])]=dist
        slst=sorted(ptdict.items(), key =
             lambda kv:(kv[1], kv[0]))
        ret=[]
        for i in range(k):
            ret.append(slst[i][0])
        return ret

# the solution below exceeds runtime

import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        smlpts=[]
        # maxlen=200000
        fil=False
        for i in range(len(points)):
            dist=math.sqrt(points[i][0]**2+points[i][1]**2)

            if i==0:
                smlpts.append((dist,points[i]))

            elif i<k:

                smlpts=self.xinsert(smlpts,(dist,points[i]),fil,k)
            elif len(smlpts)>0 and dist>smlpts[len(smlpts)-1][0]:
                pass
            else:
                fil=True
                smlpts=self.xinsert(smlpts,(dist,points[i]),fil,k)
        ret=[]
        for i in range(k):
            ret.append(smlpts[i][1])
        return ret

    def xinsert(self, smlpts,elemt,fil,k):
        # initlen=len(smlpts)
        idx=-1
        for i in range(len(smlpts)):
            if elemt[0]<smlpts[i][0]:
                idx=i
                break

        if idx==-1 and fil==False:
            smlpts.append(elemt)
            return smlpts
        elif idx>=0:
            smlpts.insert(idx,elemt)
        return smlpts[:k]

        # sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])
