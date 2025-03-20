class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        i =0
        while(i<len(asteroids)):
            if(len(stack)!=0 and (stack[len(stack)-1]>0 and asteroids[i]<0)):
                while(len(stack)!=0):
                    if(stack[len(stack)-1]<0):
                        stack.append(asteroids[i])
                        break
                    elif(stack[len(stack)-1]+asteroids[i]==0):
                        stack.pop()
                        break
                    elif(stack[len(stack)-1]+asteroids[i]>0):
                        break
                    else:
                        stack.pop()
            else:
                stack.append(asteroids[i])
            i +=1
        
        return stack 
        