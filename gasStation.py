from typing import List


class Solution:
    def canCompl(self, gas: List[int], cost: List[int]) -> int:
        
        def sim(curr):
            # print("curr:",curr)
            ori=curr
            
            gs=gas[curr]
            if gs-cost[curr]>=0:
                gs-=cost[curr]
                curr=(curr+1)%len(gas)
                gs+=gas[curr]
            else:
                return False
            
            while True:
                # print(gs,curr)
                if gs-cost[curr]>=0:
                    gs-=cost[curr]
                    curr=(curr+1)%len(gas)
                    if curr==ori:
                        break
                    gs+=gas[curr]
                else:
                    return False
            return True
        for i in range(len(gas)):
            if sim(i)==True:
                return i
        return -1
                