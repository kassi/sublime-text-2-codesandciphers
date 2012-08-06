from codesandciphers import CncTransformer

def alpha(ch):
  o = ord(ch)
  if o >= ord('a') and o <= ord('z'):
    return unicode(o - ord('a') + 1)
  if o >= ord('A') and o <= ord('Z'):
    return unicode(o - ord('A') + 1)
  return ch

class CncAlphabetCommand(CncTransformer):
  title = "A=1..Z=26"
  transformer = lambda s: "".join([alpha(ch) for ch in s]),
