# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

class Solution:
    def reorganizeString(self, s:str) -> str:
        count = Counter(s) #hashmap, count each char
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) #0(n)

        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            #most frequent except prev
            cnt, char =  heapq.heappop(maxHeap)
            res += char
            cnt -= 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, char]
        return res