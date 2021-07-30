class Solution:
    def longestStrChain(self, words: list) -> int:
        # chainLst=[]
        # pastSet=set()
        # for i in range(len(words)):
        #     pastSet.add(words[i])
        #     if chainLst==[]:
        #         chainLst.append([words[i]])
        wordsSorted=sorted(words,key=len)
        print(wordsSorted)
        firstLen=len(wordsSorted[0])
        maxChainLen=1
        for i in range(len(wordsSorted)):
            if len(wordsSorted[i])==firstLen:
                pass
            else:
                restLst=wordsSorted[i:]
                break
        for i in range(len(wordsSorted)):
            if len(wordsSorted[i])==firstLen:
                result=self.recrr(currWord=wordsSorted[i],sub_words=restLst,chainLen=1,wordLen=firstLen)
                maxChainLen=max(maxChainLen,result)
            else:
                break
        return maxChainLen
    def isDesc(self, predc:str,element:str)->bool:

        extra=0
        predcIdx=0
        print(len(predc),len(element))
        for i in range(len(element)):
            if element[i]==predc[predcIdx]:
                if predcIdx==len(predc)-1:
                    break
                predcIdx+=1
            elif extra==0:
                extra+=1
            else:
                return False
            
        
        return True
    def recrr(self,currWord:str ,sub_words:list,chainLen:int,wordLen:int)->int:
        nextLst=[]
        restLst=[]
        for i in range(len(sub_words)):
            if len(sub_words[i])==wordLen+1:
                nextLst.append(sub_words[i])
            else:
                restLst=sub_words[i:]
                break
        if len(nextLst)==0:
            return chainLen
        else:    
            maxCount=0
            for i in range(len(nextLst)):
                if  self.isDesc(currWord,nextLst[i])==True:
                    result=self.recrr(nextLst[i],restLst,chainLen+1,wordLen+1)
                    maxCount=max(result,maxCount)
                else:
                    return chainLen
                    
            return maxCount
        
        


