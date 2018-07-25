class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp=x
        final=0
        check_sign=1
        if temp < 0:
            check_sign=-1
            temp=abs(temp)
        while temp > 0:
            dig=temp%10
            temp/=10
            final= final*10+dig
        if (final)>=(2**31):
            return 0
        return final*check_sign
