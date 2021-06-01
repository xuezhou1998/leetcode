#
# use a while loop outside and a for loop inside.
# The most important thing is to avoid modifying the length of an iterable,
# in which you are currently traversing.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orglst=[]
        rotlst=[]
        frslst=[]
        ntallrot=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    # orglst.append((i,j))
                    rotlst.append((i,j))
                elif grid[i][j]==1:
                    # orglst.append((i,j))
                    frslst.append((i,j))
                else:
                    pass
        oldlsts=rotlst.copy()

        for i in range(len(rotlst)):
            if self.isAllRotten(rotlst[i],frslst,rotlst)==False:
                ntallrot.append(rotlst[i])
        ctr=0
        while True:
            oldlst=rotlst.copy()
            # print(rotlst)
            opnt=[]
            for i in ntallrot:
                up=(i[0]+1,i[1])
                down=(i[0]-1,i[1])
                left=(i[0],i[1]-1)
                right=(i[0],i[1]+1)
                if up in frslst:
                    rotlst.append(up)
                    frslst.remove(up)
                    # opfr.append(up)
                    if self.isAllRotten(up,frslst,rotlst)==False:
                        # ntallrot.append(up)
                        opnt.append(up)
                if down in frslst:
                    rotlst.append(down)
                    frslst.remove(down)
                    # opfr.append(down)
                    if self.isAllRotten(down,frslst,rotlst)==False:
                        # ntallrot.append(down)
                        opnt.append(down)
                if left in frslst:
                    rotlst.append(left)
                    frslst.remove(left)
                    # opfr.append(left)
                    if self.isAllRotten(left,frslst,rotlst)==False:
                        # ntallrot.append(left)
                        opnt.append(left)
                if right in frslst:
                    rotlst.append(right)
                    frslst.remove(right)
                    # opfr.append(right)
                    if self.isAllRotten(right,frslst,rotlst)==False:
                        # ntallrot.append(right)
                        opnt.append(right)
            for i in opnt:
                ntallrot.append(i)

            if oldlst==rotlst:
                if len(frslst)>0:
                    return -1
                else:
                    return ctr
            else:
                ctr+=1



    def isAllRotten(self,org,orglst,rotlst):
        # ajc=[]
        # for i in range(len(orglst)):
        if ((org[0]+1,org[1]) not in orglst) and ((org[0]-1,org[1]) not in orglst) and ( (org[0],org[1]+1) not in orglst) and ((org[0],org[1]-1) not in orglst):
            return True
        else:
            return False
