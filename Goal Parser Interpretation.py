class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        c=""
        i=0
        while i<len(command):
            if command[i]=="(" and command[i+1]==")":
                c+="o"
                i+=2
                continue
            elif command[i]=="(" or command[i]==")":
                i+=1
                continue
            c+=command[i]
            i+=1
        return c


        
