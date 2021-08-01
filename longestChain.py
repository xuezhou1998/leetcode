
        

class Solution:
    def longestStrChain(self, words: list) -> int:
        
        myMapIn={}
        mySet=set(words)
        for i in words:
            myMapIn[i]=1
        for i in words:

            myMapIn[i]=self.recrr(i,myMapIn,mySet)
        return max(myMapIn.values())
    def recrr(self, myWord:str,myMap: dict, mySet:set):

        # print(myWord,myMap,mySet)
        if len(myWord)==1:
            return 1
        myWordLst=list(myWord)
        perm = self.myPerm(myWordLst)
        perm =self.permuateDigits(list(perm),mySet)
        # print(perm,'perm')
        if len(perm)==0:
            return 1
        maxCount=1
        for i in perm:
            if myMap[i]>1:
                # print(myWord,myMap,"branch_1")
                maxCount=max(maxCount,1+myMap[i])
            else:
                # print(myWord,myMap,"branch_2")

                interm=self.recrr(i,myMap,mySet)
                myMap[i]=interm
                maxCount=max(maxCount,1+interm)
        return maxCount

    def permuateDigits(self,perms:list,mySet:set)->list:
        ret=[]
        for i in perms:
            # print("i",i)
            joint="".join(i)
            if joint in mySet:
                ret.append(joint)
        return ret
    def myPerm(self, perms:list)->list:
        ret=[]
        for i in range(len(perms)):
            elemt=perms.copy()
            elemt[i]=""
            

            # print(elemt,"elemt",perms,"perms")
            ret.append(elemt)
        # print(ret,"ret")
        return ret


a=Solution()
tests=[["a","b","ba","bca","bda","bdca"],
["xbc","pcxbcf","xb","cxbc","pcxbc"],
["abcd","dbqca"],["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]]
for i in tests:
    print(a.longestStrChain(i))




        
        


