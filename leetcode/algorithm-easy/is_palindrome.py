class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        string_x=str(x)
        reverse_x=string_x[::-1]
        if(string_x==reverse_x):
            return True
        return False
