class Solution:
    def maximumSwap(self, num: int) -> int:
        ret=num
        strnum=str(num)
        currMax=num
        numChged=0
        for i in range(len(strnum)-1):
            print(numChged)
            if strnum[i]==9:
                pass
            else:
                result=self.find_max_digit(strnum[i+1:])
                print(result)
                if int(strnum[i])<result[0]:
                    numLst=list(strnum)
                    oldnum=strnum[i]
                    numLst[result[1]+i+1]=oldnum
                    numLst[i]=str(result[0])
                    
                    numChged=int("".join(numLst))
                    if currMax<numChged:
                        currMax=numChged
                    else:
                        pass
            strnum=str(num)
        


                    

        return currMax
    def find_max_digit(self, strnum:str)->list[int,int]:
        numlst=list(strnum)
        maxDigit=0
        idx=0
        retidx=0
        for i in numlst:

            i=int(i)
            if maxDigit<=i:
                maxDigit=i
                retidx=idx
            idx+=1
                
        return [maxDigit,retidx]