class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        window = Counter()
        for end in range(len(s)):
            window[s[end]] += 1
            while window[s[end]] > 1:
                window[s[start]] -= 1
                start += 1
            longest = max(longest,end-start+1)
        return longest