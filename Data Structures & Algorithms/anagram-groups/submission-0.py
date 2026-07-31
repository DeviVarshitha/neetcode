class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map sorted string to a list of its anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a unique key
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return the grouped anagrams as a list of lists
        return list(anagram_map.values())
