class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        n = int(math.sqrt(area))
        while area % n != 0:
            n -= 1
        return [int(area/n),n]
        	      
		