class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas=dict()
        a=0
        b=len(height)-1
        maxarea=0
        while(b>a):
            maxarea=max(maxarea,min(height[a],height[b])*(b-a))
            if(height[a]>height[b]):
                b-=1
            else:
                a+=1
        return maxarea
