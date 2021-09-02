class Solution:
    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        myStack=[]

        while True:
            if len(pushed)==0 and len(popped)==0:
                break
            else:
                if len(myStack)>0 and myStack[-1]==popped[0]:
                    myStack.remove(myStack[-1])
                    popped.remove(popped[0])
                elif len(pushed)>0:
                    
                    myStack.append(pushed[0])
                    pushed.remove(pushed[0])
                # print(myStack)
                
                elif len(popped)>0:
                    break
                else:
                    pass
            # print(myStack)
        if len(myStack)>0:
            return False
        else:
            return True