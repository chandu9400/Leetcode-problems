
def strStr(self, haystack: str, needle: str) -> int:
        """ what if both strings are equal """
        if haystack == needle:
            return 0
        """ By using sliding window, we try to match the frame of needle in haystack """
        i = 0
        j = len(needle)
        while j <= len(haystack):
            current = haystack[i:j]
            if current == needle:
                return i
            i+=1
            j+=1 ## moving indexes for rechecking that frame.
        return -1
