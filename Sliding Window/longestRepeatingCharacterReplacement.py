class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start = 0
        window = ""
        longest = 0

        for end in range(0,len(s)):
            window += s[end]
            count = Counter(window)
            ch_max = max( count, key = count.get)
            if ( len(window) - count.get(ch_max) > k):
                window = window[1::]

            longest = max(longest,len(window))
        return longest