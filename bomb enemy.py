class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        dx={}
        dy={}
        dd={}
        # r=len(grid[0])
        # c=len(grid)
        def fx(r:List[str],j:int)->int:
            ret=0
            # for i in range(j,len(r)):
            #     if r[i]=='W':
            #         return ret
            #     elif r[i]=='E':
            #         ret+=1
            #     else:
            #         pass
            idx=j
            while j<len(r):
                if r[j]=='W':
                    break
                elif r[j]=='E':
                    ret+=1
                else:
                    pass
                j+=1
            j=idx
            while j>=0:
                if r[j]=='W':
                    break
                elif r[j]=='E':
                    ret+=1
                else:
                    pass
                j-=1
                
            return ret
        def fy(grid:List[List[str]] ,j:int,col:int)->int:
            ret=0
            idx=col
            while col<len(grid):
                if grid[col][j]=='W':
                    break
                elif grid[col][j]=='E':
                    ret+=1
                else:
                    pass
                col+=1
            col=idx
            while col>=0:
                if grid[col][j]=='W':
                    break
                elif grid[col][j]=='E':
                    ret+=1
                else:
                    pass
                col-=1
            return ret
            # for i in range(col,len(grid)):
            #     if grid[i][j]=='W':
            #         return ret
            #     elif grid[i][j]=='E':
            #         ret+=1
            #     else:
            #         pass
            # return ret
        
        print("start")
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                # print(dx,dy)
                if grid[i][j]=='W':
                    # dx.keys().remove(i)
                    # dy.keys().remove(j)
                    if i in dx.keys():
                        del dx[i]
                    if j in dy.keys():
                        del dy[j]
                    continue
                if grid[i][j]=='E':
                    continue
                
                if i not in dx.keys():
                    dx[i]=fx(grid[i],j)
                    # dd[(i,j)]=dx[i]+dy[j]
                if j not in dy.keys():
                    dy[j]=fy(grid,j,i)
                    # dd[(i,j)]=dx[i]+dy[j]
                
                dd[(i,j)]=dx[i]+dy[j]
        # print(dd.values())
        if len(list(dd.values()))!=0:
            return max(dd.values())
        else:
            return 0
        return max(dd.values())
                    
                    
        
