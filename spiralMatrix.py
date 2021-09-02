class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirc='r'
        ul=1
        dl=len(matrix)
        rl=len(matrix[0])
        ll=0
        
        ret=[]
        i=0
        j=0
        # rl=len(matrix)-1
        # cl=len(matrix[0])
        # ret.append(matrix[0][0])
        m=len(matrix)
        n=len(matrix[0])
        dirc='r'
        while len(ret)<m*n:
            if dirc=='r':
                while j<rl:
                    ret.append(matrix[i][j])
                    j+=1
                    
                j-=1
                i+=1
                dirc='d'
                
            elif dirc=='d':
                
                while i<dl:
                    ret.append(matrix[i][j])
                    i+=1
                i-=1
                j-=1
                dirc='l'
                
            elif dirc=='l':
                while j>=ll:
                    ret.append(matrix[i][j])
                    j-=1
                j+=1
                i-=1
                dirc='u'
            elif dirc=='u':
                while i>=ul:
                    ret.append(matrix[i][j])
                    i-=1
                i+=1
                j+=1
                dirc='r'
                ul+=1
                dl-=1
                rl-=1
                ll+=1
                
        return ret
                
                
