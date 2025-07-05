class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        num_psg = 0
        for i in details:
            age = i[11]+i[12]
            if(int(age)>60):
                num_psg +=1
        
        return num_psg
        