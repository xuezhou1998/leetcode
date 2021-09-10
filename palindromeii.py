class Solution:
    def validPalindrome(self, s: str) -> bool:
        h=0
        t=len(s)-1
        ret=True
        while h<t:
            if s[h]==s[t]:
                pass
            else:
                # print(s[h+1:t+1],str(reversed(s[h+1:t+1])))
                if h==t-1:
                    ret=True
                elif list(s[h+1:t+1])==list(reversed(s[h+1:t+1])):
                    
                    ret=True
                    
                elif list(s[h:t])==list(reversed(s[h:t])):
                    ret=True
                else:
                    ret=False
                break
            h+=1
            t-=1
        return ret