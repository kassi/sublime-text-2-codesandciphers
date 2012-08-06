import string
import sublime, sublime_plugin

class CncTransformer(sublime_plugin.TextCommand):
  def run(self, edit):
    self.settings = sublime.load_settings("CodesAndCiphers.sublime-settings")
    self.transform(self.transformer[0], self.view, edit)

  def transform(self, f, view, edit):
    if self.settings.get("line_mode"):

      for region in self.view.sel():
        if region.empty():
          line = self.view.line(region)
          line_contents = self.view.substr(line) + '\n'
          position = line.end()
        else:
          position = region.end()
          line_contents = self.view.substr(region)

        header = self.header()
        text = f(line_contents)
        self.view.insert(edit, position+1, header+text)

        view.sel().clear()
        view.sel().add(sublime.Region(position+len(header+text)))
    else:
      for s in view.sel():
        if s.empty():
          s = view.word(s)

        txt = f(view.substr(s))
        view.replace(edit, s, txt)

  def header(self):
    return "\n>> "+self.title+":\n"
