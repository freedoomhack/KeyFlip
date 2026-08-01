import keyboard


class HotkeyService:

    def __init__(self, callback):

        self.callback = callback

        self.current_hotkey = None

    def start(self, hotkey="ctrl+shift+m"):

        keyboard.add_hotkey(
            hotkey,
            self.callback
        )

        self.current_hotkey = hotkey

    def update(self, new_hotkey):

        if self.current_hotkey:
            keyboard.remove_hotkey(self.current_hotkey)

        keyboard.add_hotkey(
            new_hotkey,
            self.callback
        )

        self.current_hotkey = new_hotkey