'''

1. if the result is false, that node should be removed from the visited set "vs"
2. for every different starting point, you need flush the visited set "vs"
3. only when the character of the current node matches the current character of the string "word", should you add it into the visited set

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # print("start")
        vs=set()
        sz=len(board)*len(board[0])
        def dfs(word:str,cord:tuple):
            # print(word,cord,vs)
            
            if word=="":
                return True
            if word[0]==board[cord[0]][cord[1]]:
                vs.add(cord)
                if cord[0]-1>=0:
                    if (cord[0]-1,cord[1]) not in vs:
                        res=dfs(word[1:],(cord[0]-1,cord[1]))
                        if res==True:
                            
                            return True
                        else:
                            if (cord[0]-1,cord[1]) in vs:
                                vs.remove((cord[0]-1,cord[1]))
                if cord[0]+1<len(board):
                    if (cord[0]+1,cord[1]) not in vs:
                        res=dfs(word[1:],(cord[0]+1,cord[1]))
                        if res==True:
                            return True
                        else:
                            if (cord[0]+1,cord[1]) in vs:
                                vs.remove((cord[0]+1,cord[1]))
                if cord[1]-1>=0:
                    if (cord[0],cord[1]-1) not in vs:
                        res=dfs(word[1:],(cord[0],cord[1]-1))
                        if res==True:
                            return True
                        else:
                            if (cord[0],cord[1]-1) in vs:
                                vs.remove((cord[0],cord[1]-1))
                if cord[1]+1<len(board[0]):
                    if (cord[0],cord[1]+1) not in vs:
                        res=dfs(word[1:],(cord[0],cord[1]+1))
                        if res==True:
                            return True
                        else:
                            if (cord[0],cord[1]+1) in vs:
                                vs.remove((cord[0],cord[1]+1))
                if len(word)==1:
                    return True
            else:
                return False
            
            return False
        q=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if board[i][j]==word:
                        return True
                    q.append((i,j))
        for i in q:
            vs=set()
            res=dfs(word,i)
            if res==True:
                return True
        return False
        
            
            

                
                    
