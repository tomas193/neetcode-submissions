class Solution:
  def isBalanced(self, fqs: list[int]) -> bool:
    for char_sum in fqs:
      if char_sum != 0:
        return False
    return True
    
  def computeCharDiffs(self, s: str, t: str) -> list[int]:
    base_idx = ord('a')
    last_idx = ord('z')
    
    fqs = [0] * (last_idx - base_idx + 1)
    for idx in range(len(s)):
      s_idx = ord(s[idx]) - base_idx
      t_idx = ord(t[idx]) - base_idx

      fqs[s_idx] += 1
      fqs[t_idx] -= 1
    return fqs
  
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False

    fqs = self.computeCharDiffs(s, t)
    return self.isBalanced(fqs)
        