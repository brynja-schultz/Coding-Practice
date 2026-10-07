class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for word in strs:
            # if an anagram already exists
            curr_word = "".join(sorted(word))
            if curr_word in anagrams:
                anagrams[curr_word].append(word)
            # if a new anagram
            else:
                anagrams[curr_word] = [word]
        
        result = []

        for key in anagrams:
            result.append(anagrams[key])

        return result
