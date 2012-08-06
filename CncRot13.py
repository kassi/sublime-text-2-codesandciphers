from codesandciphers import CncTransformer

def rot13(ch):
  o = ord(ch)
  if o >= ord('a') and o <= ord('z'):
    return unichr((o - ord('a') + 13) % 26 + ord('a'))
  if o >= ord('A') and o <= ord('Z'):
    return unichr((o - ord('A') + 13) % 26 + ord('A'))
  return ch

class CncRot13Command(CncTransformer):
  title = "Rot 13"
  transformer = lambda s: "".join([rot13(ch) for ch in s]),
