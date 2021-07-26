# this problem is mainly about how to utilize
# stack data structure

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s=list(s)
        stack=[]
        lst=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if len(stack)>0:

                    stack.pop()
                else:
                    lst.append(i)
        for j in range(len(stack)):
            s[stack[j]]='1'
            # print(s)
        for k in range(len(lst)):
            s[lst[k]]='1'
            # print(s,lst[k])
        ret=''
        ret=ret.join(s)
        ret=ret.replace('1','')
        # print(lst,stack)
        return ret
