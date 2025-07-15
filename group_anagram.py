from typing import List  # Import List from typing module

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        print(strs)
        print(frozenset({
            "a":11,
            "d":1
        }))
        if len(strs) == 0:
            return [[""]]
        elif len(strs) == 1:
            return [strs]

        else:
            hash_dir ={}
            for char in strs:
                
                frozen_set=self.createHastable(char)
                if frozen_set in hash_dir:
                    hash_dir[frozen_set].append(char)
                else:
                    hash_dir[frozen_set]= list([char])

            return list(hash_dir.values())

    def createHastable(self, string:str):
        character_hash={}
        for char in string:
            if char in character_hash:
                character_hash[char] +=1
            else:
                character_hash[char] = 1

        return frozenset(character_hash)


solution = Solution()
result = solution.groupAnagrams(["ddddddddddg", "dgggggggggg"])
print(result)
        
