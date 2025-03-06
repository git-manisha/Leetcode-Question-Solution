class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        i =0
        while(i<len(operations)):
            if(operations[i] == '+'):
                idx = len(stack)-1
                stack.append(stack[idx]+stack[idx-1])
            elif(operations[i] == 'D'):
                stack.append(stack[len(stack)-1]*2)
            elif(operations[i] == 'C'):
                stack.pop()
            else:
                stack.append(int(operations[i]))
            i +=1
        
        result =0
        while(stack):
            result +=stack.pop()
        
        return result