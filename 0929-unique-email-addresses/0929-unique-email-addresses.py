def checkMail(mail):
        i =0
        str1 = ""
        while(i<len(mail)):
            if(mail[i] == '@'):
                while(i<len(mail)):
                    str1 = str1+mail[i]
                    i = i+1
            elif(mail[i] == '.'):
                i = i+1
            elif(mail[i] == '+'):
                while(mail[i] != '@'):
                    i= i+1
            else:
                str1 = str1+mail[i]
                i=i+1
        return str1
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = set()
        itr = 0
        while(itr<len(emails)):
            temp = checkMail(emails[itr])
            ans.add(temp)
            itr = itr+1

        count = len(ans)
        return count
