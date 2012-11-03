import sublime, sublime_plugin
import os


class OpenWithFinderCommand(sublime_plugin.WindowCommand):
  def run(self):
    import subprocess

    if self.window.active_view():
      subprocess.call(['open', '-R', self.window.active_view().file_name()])
    else:
      sublime.error_message(__name__ + ": No file to open.")
      return


  def is_visible(self):
    return sublime.platform() == 'osx'
