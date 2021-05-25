class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cdir="up"
        curr=[0,0]
        instructions=instructions*4
        for i in range(len(instructions)):
            # print(curr)
            if instructions[i]=="G":
                if cdir=="up":
                    curr=self.up(curr)
                elif cdir=="down":
                    curr=self.down(curr)
                elif cdir=="left":
                    curr=self.left(curr)
                elif cdir=="right":
                    curr=self.right(curr)
            elif instructions[i]=="L":
                if cdir=="up":
                    cdir="left"
                elif cdir=="down":
                    cdir="right"
                elif cdir=="left":
                    cdir="down"
                elif cdir=="right":
                    cdir="up"
            elif instructions[i]=="R":
                if cdir=="up":
                    cdir="right"
                elif cdir=="down":
                    cdir="left"
                elif cdir=="left":
                    cdir="up"
                elif cdir=="right":
                    cdir="down"
            print(curr)
        if curr==[0,0]:
            return True
        else:
            return False
        
    def left(self, curr):
        newcord=[0,0]
        newcord[0]=curr[0]-1
        newcord[1]=curr[1]
        return newcord
    def right(self, curr):
        newcord=[0,0]
        newcord[0]=curr[0]+1
        newcord[1]=curr[1]
        return newcord
    def up(self, curr):
        newcord=[0,0]
        newcord[0]=curr[0]
        newcord[1]=curr[1]+1
        return newcord
    def down(self, curr):
        newcord=[0,0]
        newcord[0]=curr[0]
        newcord[1]=curr[1]-1
        return newcord