class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pool={}
        for element in nums:
            if element in pool:
                pool[element]+=1
            else: 
                pool[element]=1
        lista = sorted(pool, key=pool.get, reverse=True)
        return lista[0:k]