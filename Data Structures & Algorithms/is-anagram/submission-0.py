class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        conteo1={}
        conteo2={}
        for n in s:
          if n in conteo1:
            conteo1[n]+=1
          else:
            conteo1[n]=1
        for n in t:
          if n in conteo2:
            conteo2[n]+=1
          else:
            conteo2[n]=1
        if conteo1 == conteo2:
           return True
        else:
           return False