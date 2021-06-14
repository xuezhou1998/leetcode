class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret=[]
        if len(firstList)==0 or len(secondList)==0:
            return ret
        stItem1=firstList[0][0]
        stItem2=secondList[0][0]
        if stItem1<=stItem2:
            startLst=firstList
        else:
            startLst=secondList
        indx1=0
        indx2=0
        open1=False
        open2=False
        ctr=0
        while indx1<len(firstList) and indx2<len(secondList):
            cur1=firstList[indx1]
            cur2=secondList[indx2]
            if cur1[0]>cur2[1]:
                indx2+=1 
            elif cur2[0]>cur1[1]:
                indx1+=1
            
            elif  cur1[0]>=cur2[0] and cur1[1]<=cur2[1]:
                indx1+=1
                ret.append([cur1[0],cur1[1]])
            elif  cur2[0]>=cur1[0] and cur2[1]<=cur1[1]:
                indx2+=1
                ret.append([cur2[0],cur2[1]])
            elif cur1[0]<=cur2[0] and cur1[1]<=cur2[1] and cur1[1]>=cur2[0]:
                indx1+=1
                ret.append([cur2[0],cur1[1]])
            
            elif cur2[0]<=cur1[0] and cur2[1]<=cur1[1] and cur2[1]>=cur1[0]:
                indx2+=1
                ret.append([cur1[0],cur2[1]])
            ctr+=1
            # if ctr>100:
            #     print('infinite loop')
            #     break
             
            
            

        return  ret