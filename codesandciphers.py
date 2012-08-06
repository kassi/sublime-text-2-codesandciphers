import string
import sublime, sublime_plugin

class CncTransformer(sublime_plugin.TextCommand):
  def run(self, edit):
    self.transform(self.transformer[0], self.view, edit)

  def transform(self, f, view, edit):
    for s in view.sel():
      if s.empty():
        s = view.word(s)

      txt = f(view.substr(s))
      view.replace(edit, s, txt)
