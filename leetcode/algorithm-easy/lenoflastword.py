class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=0
        count=0
        for letter in reversed(s):
            if letter != " ":
                length+=1
            elif length!=0 and letter == " ":
                return length
        return length
                
