class Solution(object):
    def binaryGap(self, N):
        binary=bin(N)
        flag=0
        fullength=0
        curlength=0
        for i in reversed(binary):
            if i=="b":
                return fullength
            if i=="1":
                if flag==1 and curlength>fullength:
                    fullength=curlength
                curlength=1
                flag=1
            else:
                curlength+=1

        return  fullength
