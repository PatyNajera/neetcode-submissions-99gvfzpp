class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        conteo_prefijos = {0: 1}
        prefix = 0
        total = 0

        for num in nums:
            prefix += num

            if prefix - k in conteo_prefijos:
                total += conteo_prefijos[prefix - k]

            if prefix in conteo_prefijos:
                conteo_prefijos[prefix] += 1
            else:
                conteo_prefijos[prefix] = 1

        return total