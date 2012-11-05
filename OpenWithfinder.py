import sublime, sublime_plugin
import os

class OpenWithFinderCommand(sublime_plugin.WindowCommand):
  def run(self, paths = [], application = "", extensions = ""):
    import sys
    import subprocess
    application_dir, application_name = os.path.split(application)
    application_dir  = application_dir.encode(sys.getfilesystemencoding())
    application_name = application_name.encode(sys.getfilesystemencoding())
    application      = application.encode(sys.getfilesystemencoding())

    if self.window.active_view():

      if sublime.platform() == 'osx':
        # osx
        subprocess.call(['open', '-R', self.window.active_view().file_name()])

      elif sublime.platform() == 'windows':
        # windows
        subprocess.Popen(r'explorer /select, "' + self.window.active_view().file_name() + '"')
      else:
        # linux
        # subprocess.call(['open', '-R', self.window.active_view().file_name()])
        return


    else:
      sublime.error_message(__name__ + ": No file to open.")
      return
