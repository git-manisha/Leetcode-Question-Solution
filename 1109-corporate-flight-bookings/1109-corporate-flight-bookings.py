class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        answer = [0]*(n+1)
        i = 0
        while(i<len(bookings)):
            l = bookings[i][0]-1
            r = bookings[i][1]-1
            
            answer[l] +=bookings[i][2]
            answer[r+1] -=bookings[i][2]
            i +=1
        
        i = 1
        while(i<len(answer)):
            answer[i] = answer[i]+answer[i-1]
            i +=1
        
        answer.pop()
        return answer
        