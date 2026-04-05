class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     conteo={}
     for n in nums:
      if n in conteo:
        return True
      conteo[n]=1
     return False
    