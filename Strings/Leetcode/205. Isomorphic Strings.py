# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomporphic(self, s:str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}
        
        for i in range(len(s)):
            if s[i] in s_map:
                if s_map[s[i]] != t[i]:
                    return False
            elif t[i] in t_map:
                if t_map[t[i]] != s[i]:
                    return False
            else:
                s_map[s[i]] = t[i]
                t_map[t[i]] = s[i]
                
        return True