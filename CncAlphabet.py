from codesandciphers import CncTransformer

"""
En/Decoder for Alphabet Code
Try it here

TRY ME

should result in (A=1,Z=26)
201825 135

TRY ME

should result in (A=26,Z=1)
792 1422

"""

def _a1z26(ch):
  o = ord(ch)
  if o >= ord('a') and o <= ord('z'):
    return unicode(o - ord('a') + 1)
  if o >= ord('A') and o <= ord('Z'):
    return unicode(o - ord('A') + 1)
  return ch

def _a26z1(ch):
  o = ord(ch)
  if o >= ord('a') and o <= ord('z'):
    return unicode(26 - (o - ord('a')))
  if o >= ord('A') and o <= ord('Z'):
    return unicode(26 - (o - ord('A')))
  return ch

class CncAlphabetCommand(CncTransformer):
  def run(self, edit, method="a1z26"):
    if method == "a1z26":
      self.title = "A=1..Z=26"
      f = _a1z26
    elif method == "a26z1":
      self.title = "A=26..Z=1"
      f = _a26z1
    # elif method == "1a26z":
    #   self.title = "1=A..26=Z"
    #   f = _1a26z
    # elif method == "26a1z":
    #   self.title = "26=A..1=Z"
    #   f = _26a1z
    self.transformer = lambda s: "".join([f(ch) for ch in s]),
    super(CncAlphabetCommand, self).run(edit)

