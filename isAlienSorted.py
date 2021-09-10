class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        olst=list(order)
        print("start")
        def islg(word1,word2)->bool:
            ret=True
            mxl=max(len(word1),len(word2))
            wlg=word1
            wsm=word2
            
            for i in range(mxl):
                
                
                if i<len(wlg):
                    od1=olst.index(wlg[i])
                    
                else:
                    ret=True
                    break
                if i<len(wsm):
                    od2=olst.index(wsm[i])
                else:
                    ret=False
                    break
                
                if od1<od2:
                    True
                    break
                elif od1==od2:
                    ret=True
                    
                else:
                    ret=False
                    break
            # print(ret)
            return ret
        for i in range(len(words)-1):
            res=islg(words[i],words[i+1])
            if res==False:
                ret=False
                break
            else:
                ret=True
        return ret
                
            