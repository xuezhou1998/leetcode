class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d=set(wordDict.copy())
        nd=wordDict.copy()
        for i in list(d):
            if i==s:
                return True
        while True:
            # print(d)
            nd=set()
            for i in list(d):
                for j in list(d):
                    if len(i+j)<=len(s):
                        if i+j==s:
                            return True
                        else:
                            if i+j not in d:
                                if i+j in s:
                                    
                                    nd.add(i+j)
                    
            if nd==set():
                return False
            else:
                d=d.union(nd)
        
                    

        
        
