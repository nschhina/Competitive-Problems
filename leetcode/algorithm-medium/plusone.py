class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size=len(digits)
        retlist=list()
        carryover=0
        for i in reversed(range(size)):
            if i==size-1:
                if(digits[i]+1==10):
                    retlist.extend([0])
                    carryover=1
                    if i==0:
                        retlist.extend([1])
                        carryover=0
                else:
                    retlist.extend([digits[i]+1])

            else:
                if carryover+digits[i]==10:
                    retlist.extend([0])
                    carryover=1
                    if i==0:
                        retlist.extend([1])
                        carryover=0
                else:
                    retlist.extend([digits[i]+carryover])
                    carryover=0
        return retlist[::-1]
        
