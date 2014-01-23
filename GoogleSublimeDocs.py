import sublime, sublime_plugin
import urllib
import webbrowser

class GoogleSublimeCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel(
            "Search for:",
            "",
            self.on_done,
            None,
            None
        )
        pass

    def on_done(self, text):
        webbrowser.open(
            "https://www.google.com/search?q=sublime+text+3+" +
            urllib.parse.quote(text)
        )
