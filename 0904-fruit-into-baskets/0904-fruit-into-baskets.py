class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        hashmap = {}
        left = 0
        right = 0
        max_count = 0
        while(right < len(fruits)):    
            if(fruits[right] in hashmap):
                hashmap[fruits[right]] +=1
            else:
                hashmap[fruits[right]] = 1

            while(left<=right and len(hashmap)==3):
                hashmap[fruits[left]] -=1
                if(hashmap[fruits[left]] == 0):
                    del hashmap[fruits[left]]
                left +=1

            max_count = max(max_count,(right-left+1))
            right +=1
        
        return max_count
        