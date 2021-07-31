# class Solution:
#     def longestStrChain(self, words: list) -> int:
#         # chainLst=[]
#         # pastSet=set()
#         # for i in range(len(words)):
#         #     pastSet.add(words[i])
#         #     if chainLst==[]:
#         #         chainLst.append([words[i]])
#         wordsSorted=sorted(words,key=len)
#         print(wordsSorted)
#         firstLen=len(wordsSorted[0])
#         maxChainLen=1
#         for i in range(len(wordsSorted)):
#             if len(wordsSorted[i])==firstLen:
#                 pass
#             else:
#                 restLst=wordsSorted[i:]
#                 break
#         for i in range(len(wordsSorted)):
#             if len(wordsSorted[i])==firstLen:
#                 result=self.recrr(currWord=wordsSorted[i],sub_words=restLst,chainLen=1,wordLen=firstLen)
#                 maxChainLen=max(maxChainLen,result)
#             else:
#                 break
#         return maxChainLen
#     def isDesc(self, predc:str,element:str)->bool:

#         extra=0
#         predcIdx=0
#         print(len(predc),len(element))
#         for i in range(len(element)):
#             if element[i]==predc[predcIdx]:
#                 if predcIdx==len(predc)-1:
#                     break
#                 predcIdx+=1
#             elif extra==0:
#                 extra+=1
#             else:
#                 return False
            
        
#         return True
#     def recrr(self,currWord:str ,sub_words:list,chainLen:int,wordLen:int)->int:
#         nextLst=[]
#         restLst=[]
#         for i in range(len(sub_words)):
#             if len(sub_words[i])==wordLen+1:
#                 nextLst.append(sub_words[i])
#             else:
#                 restLst=sub_words[i:]
#                 break
#         if len(nextLst)==0:
#             return chainLen
#         else:    
#             maxCount=0
#             for i in range(len(nextLst)):
#                 if  self.isDesc(currWord,nextLst[i])==True:
#                     result=self.recrr(nextLst[i],restLst,chainLen+1,wordLen+1)
#                     maxCount=max(result,maxCount)
#                 else:
#                     return chainLen
                    
#             return maxCount

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
        print(sub_words, "sub_words")
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
                print(currWord,nextLst[i],"c,n")
                if  self.isDesc(currWord,nextLst[i])==True:
                    result=self.recrr(nextLst[i],restLst,chainLen+1,wordLen+1)
                    maxCount=max(result,maxCount)
                else:
                    # return chainLen
                    # pass
                    maxCount=max(chainLen,maxCount)
                    
            return maxCount
        
        

# flawed
class Solution:
    def longestStrChain(self, words: list) -> int:
        # chainLst=[]
        # pastSet=set()
        # for i in range(len(words)):
        #     pastSet.add(words[i])
        #     if chainLst==[]:
        #         chainLst.append([words[i]])
        # wordsSorted=sorted(words,key=len)
        wordsSorted=words
        print(wordsSorted)
        firstLen=len(wordsSorted[0])
        lenDict={}
        currLen=-1
        for i in range(len(wordsSorted)):
            if len(wordsSorted[i])==currLen:
                if currLen not in lenDict.keys():
                    lenDict[currLen]=[wordsSorted[i]]
                else:
                    lenDict[currLen].append(wordsSorted[i])
            else:
#                 if len(wordsSorted[i])==currLen+1:
                    
                currLen=len(wordsSorted[i])
#                 else:
#                     break
                if currLen not in lenDict.keys():
                    lenDict[currLen]=[wordsSorted[i]]
                else:
                    lenDict[currLen].append(wordsSorted[i])
        # if currLen==firstLen:
        #     return 1
        maxChainLen=1
        # for i in range(len(wordsSorted)):
        #     if len(wordsSorted[i])==firstLen:
        #         pass
        #     else:
        #         restLst=wordsSorted[i:]
        #         break
        result=1
        firstLen=min(lenDict.keys())
        for i in range(len(wordsSorted)):
            if len(wordsSorted[i])==firstLen:
                if firstLen+1 in lenDict.keys():
                    
                    result=self.recrr(myDict=lenDict,currWord=wordsSorted[i],sub_words=lenDict[firstLen+1],chainLen=1,wordLen=firstLen)
                maxChainLen=max(maxChainLen,result)
            else:
                break
        return maxChainLen
    def isDesc(self, predc:str,element:str)->bool:

        extra=0
        predcIdx=0
        # print(len(predc),len(element))
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
    def recrr(self,myDict,currWord:str ,sub_words:list,chainLen:int,wordLen:int)->int:
        print(sub_words,chainLen, "sub_words","chainLen")
        nextLst=sub_words
        if wordLen+2 in myDict.keys():
            restLst=myDict[wordLen+2]
        else:
            restLst=[]
        # for i in range(len(sub_words)):
        #     if len(sub_words[i])==wordLen+1:
        #         nextLst.append(sub_words[i])
        #     else:
        #         restLst=sub_words[i:]
        #         break
        if len(nextLst)==0:
            return chainLen
        else:    
            maxCount=chainLen
            for i in range(len(nextLst)):
                print(currWord,nextLst[i],"c,n")
                if  self.isDesc(currWord,nextLst[i])==True:
                    result=self.recrr(myDict,nextLst[i],restLst,chainLen+1,wordLen+1)
                    maxCount=max(result,maxCount)
                else:
                    # return chainLen
                    # pass
                    result=self.recrr(myDict,nextLst[i],restLst,1,wordLen+1)
                    maxCount=max(result,maxCount)
                    
            return maxCount
        
        
# flawed2
class Solution:
    def longestStrChain(self, words: list) -> int:
        # chainLst=[]
        # pastSet=set()
        # for i in range(len(words)):
        #     pastSet.add(words[i])
        #     if chainLst==[]:
        #         chainLst.append([words[i]])
        # wordsSorted=sorted(words,key=len)
        wordsSorted=words
        # print(wordsSorted)
        # firstLen=len(wordsSorted[0])
        lenDict={}
        currLen=-1
        for i in range(len(wordsSorted)):
            currLen=len(wordsSorted[i])
            if currLen not in lenDict.keys():
                lenDict[currLen]=[wordsSorted[i]]
            else:
                lenDict[currLen].append(wordsSorted[i])
#             if len(wordsSorted[i])==currLen:
#                 if currLen not in lenDict.keys():
#                     lenDict[currLen]=[wordsSorted[i]]
#                 else:
#                     lenDict[currLen].append(wordsSorted[i])
#             else:
# #                 if len(wordsSorted[i])==currLen+1:
                    
#                 currLen=len(wordsSorted[i])
# #                 else:
# #                     break
#                 if currLen not in lenDict.keys():
#                     lenDict[currLen]=[wordsSorted[i]]
#                 else:
#                     lenDict[currLen].append(wordsSorted[i])
        # if currLen==firstLen:
        #     return 1
        maxChainLen=1
        # for i in range(len(wordsSorted)):
        #     if len(wordsSorted[i])==firstLen:
        #         pass
        #     else:
        #         restLst=wordsSorted[i:]
        #         break
        result=1
        firstLen=min(lenDict.keys())
        print(firstLen)
        for i in range(len(lenDict[firstLen])):
            if len(lenDict[firstLen][i])==firstLen:
                if firstLen+1 in lenDict.keys():
                    
                    result=self.recrr(myDict=lenDict,currWord=lenDict[firstLen][i],sub_words=lenDict[firstLen+1],chainLen=1,wordLen=firstLen)
                maxChainLen=max(maxChainLen,result)
            else:
                break
        return maxChainLen
    def isDesc(self, predc:str,element:str)->bool:

        extra=0
        predcIdx=0
        # print(len(predc),len(element))
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
    def recrr(self,myDict,currWord:str ,sub_words:list,chainLen:int,wordLen:int)->int:
        # print(sub_words,chainLen, "sub_words","chainLen")
        nextLst=sub_words
        if wordLen+2 in myDict.keys():
            restLst=myDict[wordLen+2]
        else:
            restLst=[]
        # for i in range(len(sub_words)):
        #     if len(sub_words[i])==wordLen+1:
        #         nextLst.append(sub_words[i])
        #     else:
        #         restLst=sub_words[i:]
        #         break
        if len(nextLst)==0:
            return chainLen
        else:    
            maxCount=chainLen
            for i in range(len(nextLst)):
                # print(currWord,nextLst[i],"c,n")
                if  self.isDesc(currWord,nextLst[i])==True:
                    result=self.recrr(myDict,nextLst[i],restLst,chainLen+1,wordLen+1)
                    maxCount=max(result,maxCount)
                else:
                    # return chainLen
                    # pass
                    result=self.recrr(myDict,nextLst[i],restLst,1,wordLen+1)
                    maxCount=max(result,maxCount)
                    
            return maxCount
        
        
class Solution:
    def longestStrChain(self, words: list) -> int:
        maxLen=0

        return maxLen
    def recrr()



        
        


