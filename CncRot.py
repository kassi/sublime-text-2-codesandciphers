from codesandciphers import CncTransformer

def rot(ch, n):
  o = ord(ch)
  if o >= ord('a') and o <= ord('z'):
    return unichr((o - ord('a') + n) % 26 + ord('a'))
  if o >= ord('A') and o <= ord('Z'):
    return unichr((o - ord('A') + n) % 26 + ord('A'))
  return ch

class CncRotCommand(CncTransformer):
  title = "Rot 1-26"
  transformer = lambda s: "".join( ["".join([rot(ch, n) for ch in s]) for n in range(0,26)] ),
