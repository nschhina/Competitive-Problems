class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        powercnt=0
        asum=0
        for str in reversed(a):
            asum+=int(str)*(2**powercnt)
            powercnt+=1
        powercnt=0
        bsum=0
        for str in reversed(b):
            bsum+=int(str)*(2**powercnt)
            powercnt+=1
        finalsum=bin(asum+bsum)
        return finalsum[2:]
