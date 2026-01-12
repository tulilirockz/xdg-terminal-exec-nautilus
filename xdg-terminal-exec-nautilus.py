from gi.repository import Nautilus, GObject, Gio
import gi
gi.require_version('Nautilus', '4.1')

class TerminalMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(self, files):
        return get_items_for_files('TerminalNautilus::open_in_terminal', files)

    def get_background_items(self, file):
        return get_items_for_files('TerminalNautilus::open_folder_in_terminal', [file])

def open_in_terminal_activated(_menu, paths):
    for path in paths:
        Gio.Subprocess.new(['systemd-run', '--user', '--collect', '--ignore-failure', '--quiet', 'xdg-terminal-exec', f'--dir={path}'], Gio.SubprocessFlags.NONE)

def get_items_for_files(name, files):
    paths = []
    for file in files:
        location = file.get_location() if file.is_directory() else file.get_parent_location()
        path = location.get_path()
        if path and path not in paths:
            paths.append(path)
    if len(paths) > 5:
        return []
    if not paths:
        return []

    item = Nautilus.MenuItem(name=name, label='Open in Terminal', icon='foot')
    item.connect('activate', open_in_terminal_activated, paths)
    return [item]
