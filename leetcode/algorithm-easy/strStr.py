class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle=="" or haystack==needle):
            return 0
        substrs=dict()
        strlen=len(needle)
        haylen=len(haystack)
        if(strlen>haylen):
            return -1
        for i in range(haylen):
            k=i+strlen
            if(k>haylen):
                break
            if(haystack[i:k] not in substrs):
                substrs[haystack[i:k]]=i
        if needle in substrs:
            return substrs[needle]
        return -1
