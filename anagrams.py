"""
Write a function, anagrams, that takes in two strings as arguments. 
The function should return a boolean indicating whether or not the strings are anagrams. 
Anagrams are strings that contain the same characters, but in any order.
"""

# Bruteforce
def anagrams(s1, s2):
  c = 0
  for i in range(len(s1)):
    s1_char = s1[i]
    for j in range(len(s2)):
      if s2[j] == s1_char:
        s2 = s2[:j] + s2[j+1:]
        c += 1
        break
  if (c != len(s1)) or (s2 != ''):
    return False
  else:
    return True

# test
anagrams('tax', 'taxi')

anagrams('cats', 'tocs')

anagrams('monkeyswrite', 'newyorktimes')

anagrams('paper', 'reapa')