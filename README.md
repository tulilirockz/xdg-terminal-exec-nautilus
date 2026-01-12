# xdg-terminal-exec-nautilus

Loadable [nautilus-python](https://wiki.gnome.org/Projects/NautilusPython) extension for [xdg-terminal-exec](https://github.com/Vladimir-csp/xdg-terminal-exec)

This adds an option on Nautilus that allows you to open a certain directory with the the xdg-terminal-exec tool, allowing for any arbitrary terminal to be used.

<img width="286" height="335" alt="image" src="https://github.com/user-attachments/assets/3f48d93f-e4a5-4f91-a1b8-23c85bf13acc" alt="Nautilus context menu showing Open in Terminal option"/>

## Installation

Place the main `xdg-terminal-exec-nautilus.py` file under any directory recognized by `nautilus-python`, that is `/usr/share/nautilus-python/extensions` or `~/.local/share/nautilus-python/extensions`.

Nautilus should load the extension after doing that.
