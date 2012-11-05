import sublime, sublime_plugin
import os

class OpenWithFinderCommand(sublime_plugin.WindowCommand):
  def run(self):
    import subprocess

    if self.window.active_view():

      if sublime.platform() == 'osx':
        # osx
        subprocess.call(['open', '-R', self.window.active_view().file_name()])

      elif sublime.platform() == 'windows':
        # windows
        subprocess.Popen(r'explorer /select, "' + self.window.active_view().file_name() + '"')

    else:
      sublime.error_message(__name__ + ": No file to open.")
