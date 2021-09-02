# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ns=nestedList
        self.flst=self.flt(nestedList)
        
        # print(self.flst)
        self.cidx=0
        # self.hidx=0
    def next(self) -> int:
        ret=self.flst[self.cidx]
        self.cidx+=1
        return ret
        
    
    def hasNext(self) -> bool:
        if self.cidx<len(self.flst):
            return True
        else:
            return False
            
    
    def flt(self,nestedList)->List:
        ns=nestedList
        fllst=[]
        for i in range(len(ns)):
            if ns[i].isInteger()==True:
                fllst.append(ns[i].getInteger())
            else:
                res=self.flt(ns[i].getList())
                for i in res:
                    fllst.append(i)
        return fllst
                

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
