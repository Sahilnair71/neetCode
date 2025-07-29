# Longest Repeating Character Replacement
# Solved 
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# complexity:
# time_complexity= O(n)
# space_complexity= O(n)


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count_hash = {}
        max_freq = 0
        result = 0
        l = 0

        for i in range(len(s)):
            if s[i] in count_hash:
                count_hash[s[i]] += 1
            else:
                count_hash[s[i]] = 1

            max_freq = max(max_freq, count_hash[s[i]])

            # If the number of characters to replace exceeds k, shrink the window
            if (i - l + 1 - max_freq) > k:
                count_hash[s[l]] -= 1
                l += 1

            # Update the result with the maximum length of valid substring
            result = max(result, i - l + 1)

        return result




        