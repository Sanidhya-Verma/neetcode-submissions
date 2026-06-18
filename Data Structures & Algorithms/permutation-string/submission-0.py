class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right  = len(s1)-1
        perm = {}
        record = {}
        if (len(s1) > len(s2)):
            return False

        for i in s1:
            perm[i]= perm.get(i,0)+1
        
        for j in range(len(s1)):
            record[s2[j]]= record.get(s2[j],0)+1

        while (right < len(s2)):
                      
            if (perm == record):
                return True
                
            else :
                record[s2[left]] = record.get(s2[left],0) -1
                if (record[s2[left]] == 0):
                    del record[s2[left]]
                left +=1
                right +=1
                if right < len(s2):
                    record[s2[right]] = record.get(s2[right],0) +1
        return False
                
                
            
            
