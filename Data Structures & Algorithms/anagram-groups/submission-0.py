class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for palabra in strs:
            clave = ''.join(sorted(palabra))
            if clave in dic:
                dic[clave].append(palabra)
            else:
                dic[clave]=[palabra]
        return list(dic.values())