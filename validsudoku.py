import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[]
        cols=[]
        lst=[]
        for i in range(3):
            for j in range(3):
                lst.append((i,j))
        nine={}
        cols=[]
        for i in lst:
            nine[i]=set()
            cols.append(set())
        print(nine)
        for i in range(len(board)):
            row=set()
            
            for j in range(len(board[0])):
                print(board[i][j])
                if board[i][j] in row:
                    print("b1")
                    return False
                elif board[i][j].isdigit()==True:
                    print("b2")
                    row.add(board[i][j])
                if board[i][j] in cols[j]:
                    print("b1")
                    return False
                elif board[i][j].isdigit()==True:
                    print("b2")
                    cols[j].add(board[i][j])
                idx1=math.ceil((i+1)/3)-1
                idx2=math.ceil((j+1)/3)-1
                if board[i][j] in nine[(idx1,idx2)]:
                    print("b3")
                    return False
                    
                elif board[i][j].isdigit()==True:
                    print("b4")
                    nine[(idx1,idx2)].add(board[i][j])
        return True
                
                
                
