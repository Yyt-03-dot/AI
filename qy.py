class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left=0
        dict1={}
        dict2={}
        result=[]
        for i in p:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
         for right in range(len(s)):
            if right-left+1 > len(p):
                dict2-=1
                left+=1
            dict1[i]+=1
            if right-left+1 == len(p) and dict1==dict2:
                result.append(left)
        return result