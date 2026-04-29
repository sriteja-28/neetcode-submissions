class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups={}
        # for word in strs:
        #     key="".join(sorted(word))
        #     if key not in groups:
        #         groups[key]=[]
        #     groups[key].append(word)
        # return list(groups.values())

        # groups=defaultdict(list)
        # for word in strs:
        #     key="".join(sorted(word))
        #     groups[key].append(word)
        # return list(groups.values())

        groups=defaultdict(list)
        for word in strs:
            count=[0]*26
            for ch in word:
                count[ord(ch)-ord("a")]+=1
            groups[tuple(count)].append(word)
        return list(groups.values())
        


        