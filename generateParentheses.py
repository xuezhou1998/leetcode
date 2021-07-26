class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[]
        newlst=[]
        for i in range(2*n):
            if lst==[]:
                lst.append('(')
                lst.append(')')
            else:
                newlst=[]
                for k in range(len(lst)):
                    newlst.append(lst[k]+')')
                    newlst.append(lst[k]+'(')
                lst=newlst.copy()
        ret=[]
        for i in range(len(lst)):
            if self.isWF(lst[i])==True:
                ret.append(lst[i])
        return ret
    def isWF(self, s:str)->bool:
        stack=[]
        for i in range(len(s)):
            if (s[i]=="("):
                stack.append('(')
            elif (s[i]==")"):
                if len(stack)>0:
                    stack.pop()
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False
        
