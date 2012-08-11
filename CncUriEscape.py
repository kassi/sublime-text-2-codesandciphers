from codesandciphers import CncTransformer
import urllib

class CncUriEscapeCommand(CncTransformer):
  title = "URI Escape"
  transformer = lambda s:urllib.quote_plus(s),

class CncUriUnescapeCommand(CncTransformer):
  title = "URI Unescape"
  transformer = lambda s:urllib.unquote_plus(s),

