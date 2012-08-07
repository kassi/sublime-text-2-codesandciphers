# -*- coding: utf-8 -*-
from codesandciphers import CncTransformer
import re

"""
Workaround for Sublime console
"""
import sys
import codecs

def setup_console(sys_enc="utf-8"):
    """
    Set sys.defaultencoding to `sys_enc` and update stdout/stderr writers to corresponding encoding
    For Win32 the OEM console encoding will be used istead of `sys_enc`
    """
    reload(sys)
    try:
        if sys.platform.startswith("win"):
            import ctypes
            enc = "cp%d" % ctypes.windll.kernel32.GetOEMCP() #TODO: win64/python64 implementation
        else:
            enc = (sys.stdout.encoding if sys.stdout.isatty() else
                        sys.stderr.encoding if sys.stderr.isatty() else
                            sys.getfilesystemencoding() or sys_enc)

        sys.setdefaultencoding(sys_enc)

        # redefine stdout/stderr in console
        if sys.stdout.isatty() and sys.stdout.encoding != enc:
            sys.stdout = codecs.getwriter(enc)(sys.stdout, 'replace')

        if sys.stderr.isatty() and sys.stderr.encoding != enc:
            sys.stderr = codecs.getwriter(enc)(sys.stderr, 'replace')

    except:
        pass

setup_console()


"""
Leetspeak decoder

/\|>ß@

may result in
ABBA

1337 \/\/1|<1P3[)14

may result in
LEET WIKIPEDIA

"""

table = {
  u"A": [ u"4", u"@", u"/\\", u"/-\\", u"?", u"^", u"α", u"λ" ],
  u"B": [ u"8", u"|3", u"ß", u"l³", u"P>", u"13", u"I3" ],
  u"C": [ u"(", u"[", u"<", u"©", u"¢" ],
  u"D": [ u"|)", u"|]", u"Ð", u"đ", u"1)", u"|>", u"[)" ],
  u"E": [ u"3", u"€", u"&", u"£", u"ε" ],
  u"F": [ u"|=", u"PH", u"|*|-|", u"|\"", u"ƒ", u"l²" ],
  u"G": [ u"6", u"&", u"9" ],
  u"H": [ u"4", u"|-|", u"#", u"}{", u"]-[", u"/-/", u")-(" ],
  u"I": [ u"!", u"1", u"|", u"][", u"ỉ" ],
  u"J": [ u"_|", u"¿" ],
  u"K": [ u"|<", u"|{", u"|(", u"X" ],
  u"L": [ u"1", u"|_", u"£", u"|", u"][_" ],
  u"M": [ u"/\\/\\", u"/v\\", u"|V|", u"]V[", u"|\\/|", u"AA", u"[]V[]", u"|11", u"/|\\", u"^^", u"(V)"u"|Y|" ],
  u"N": [ u"|\\|", u"/\\/", u"/V", u"|V", u"/\\\\/", u"|1", u"2", u"?", u"(\\)", u"11", u"r," ],
  u"O": [ u"0", u"9", u"()", u"[]", u"*", u"°", u"<>", u"ø", u"{[]}" ],
  u"P": [ u"|°", u"p", u"|>", u"|*", u"[]D", u"][D", u"|²", u"|?", u"|D" ],
  u"Q": [ u"0_", u"0," ],
  u"R": [ u"2", u"|2", u"1²", u"®", u"?", u"я", u"12", u".-" ],
  u"S": [ u"5", u"$", u"§", u"?", u"ŝ", u"ş" ],
  u"T": [ u"7", u"+", u"†", u"']['", u"|" ],
  u"U": [ u"|_|", u"µ", u"[_]", u"v" ],
  u"V": [ u"\\/", u"|/", u"\\|", u"\\'" ],
  u"W": [ u"\\/\\/", u"VV", u"\\A/", u"\\\\'", u"uu", u"\\^/", u"\\|/" ],
  u"X": [ u"><", u")(", u"}{", u"%", u"?", u"×", u"][" ],
  u"Y": [ u"`/", u"°/", u"9", u"¥" ],
  u"Z": [ u"z", u"2", u"\"/_" ],
  u"Ä": [ u"43", u"°A°", u"°4°" ],
  u"Ö": [ u"03", u"°O°" ],
  u"Ü": [ u"|_|3", u"°U°" ],
}
mapping = {}
def init():
  if not mapping:
    for letter in table.keys():
      for elem in table[letter]:
        mapping[elem] = letter

def decode(x):
  g = x.group(0)
  return mapping[g]

def leet(s):
  init()
  glyphs = sorted(mapping.keys(),None,None,True)
  escaped_glyphs = map(re.escape,glyphs)
  regex = u"(" + u"|".join(escaped_glyphs) + u")"
  pattern = re.compile(regex, re.UNICODE)
  result = pattern.sub(decode, unicode(s))
  return result

class CncLeetspeakCommand(CncTransformer):
  title = "Leetspeak decoder"
  transformer = [leet]
