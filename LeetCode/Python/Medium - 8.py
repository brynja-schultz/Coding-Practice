class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        curr_arr = s[0:len(p)]

        og_freq = {}
        freq_dict = {}
        
        for char in p:
            if char in og_freq:
                og_freq[char] += 1
            else:
                og_freq[char] = 1

        for char in curr_arr:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1       

        for i in range(len(s) - len(p) + 1):
            if og_freq == freq_dict:
                result.append(i)
            if i != len(s) - len(p):
                freq_dict[s[i]] -= 1 
                if freq_dict[s[i]] == 0:
                    freq_dict.pop(s[i])

                if s[i+len(p)] in freq_dict:
                    freq_dict[s[i+len(p)]] += 1
                else:
                    freq_dict[s[i+len(p)]] = 1 

        return result
