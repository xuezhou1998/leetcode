#
# crt is used to keep the latest position, and use a stack to
# keep track of the closest outer layer. use the difference between the
# crt and the position of a new start or end to calculate the time period,
# and add it to either the outer or current layer depending on different
# three cases below
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # print('xxxxxxxxxx')
        fdict={}
        logstk=[]
        crt=0
        for i in range(n):
            fdict[i]=0
        for i in range(len(logs)):
            fmt=self.getform(logs[i])

            if logstk==[]:
                logstk.append(fmt)
                # crt=fmt[2]
                # crt=fmt[2]
            elif logstk[-1][1]=='start' and fmt[1]=='end':
                # crt=fmt[2]

                fdict[logstk[-1][0]]+=fmt[2]-crt+1
                crt=fmt[2]+1


                logstk.pop()
            elif logstk[-1][1]=='start' and fmt[1]=='start':
                fdict[logstk[-1][0]]+=fmt[2]-crt
                logstk.append(fmt)
                crt=fmt[2]
            # print(crt)
            # print(fdict)
            # print(logstk)


        ret=[]
        for i in sorted(fdict.keys()):
            ret.append(fdict[i])
        return ret
    def getform(self,log:str):
        loglst=log.split(':')
        return (int(loglst[0]),str(loglst[1]),int(loglst[2]))
