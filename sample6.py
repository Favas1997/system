import string

def panagram(s):
    alphabets = set(string.ascii_lowercase)
    print(set(s.lower()) >= alphabets)
s = "The quick brown fox jumps over the lazy dog"
panagram(s)