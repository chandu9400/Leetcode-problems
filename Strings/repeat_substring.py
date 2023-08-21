## Leetcode(459). Repeated Substring Pattern

## Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
## Example 1:

## Input: s = "abab"
## Output: true
## Explanation: It is the substring "ab" twice.
## Example 2:

## Input: s = "aba"
## Output: false
## Example 3:

## Input: s = "abcabcabcabc"
## Output: true
## Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
## Constraints:

## 1 <= s.length <= 10^4 , s consists of lowercase English letters.


## Code

def repeatedSubstringPattern(self, s: str) -> bool:
  #making a superset of string s
  s_fold = list(s[1:]) + list(s[:-1])
  superset = "".join(s_fold)
  return s in superset





