# Permutation in String
# Solved 
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Complexity:
# Time: O(m*n) not optimal

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        tem_hash = {}
        
        # Build frequency map for s1
        for i in s1:
            if i in tem_hash:
                tem_hash[i] += 1
            else:
                tem_hash[i] = 1
        
        # Iterate over s2, checking substrings of length s1_len
        for i in range(len(s2) - s1_len + 1):  # Loop over valid starting indices in s2
            local_hash = tem_hash.copy()  # Make a copy of tem_hash for each window
            all_matched = True  # Flag to track if the substring is a valid permutation
            
            # Check if substring matches the frequency map
            for k in range(s1_len):
                print(i + k, "i+k")
                print(local_hash)
                if s2[i + k] in local_hash and local_hash[s2[i + k]] > 0:
                    local_hash[s2[i + k]] -= 1  # Decrement the count of the matched character
                    print(local_hash)
                else:
                    all_matched = False
                    break
            
            # If inner loop completes and all characters are matched
            if all_matched:
                return True

        return False


