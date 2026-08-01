import time
import pyperclip
import keyboard


class ClipboardService:

    def __init__(self):

        self.previous_clipboard = ""

    def get_selected_text(self, retries=4, delay=0.2):

        self.previous_clipboard = pyperclip.paste()

        pyperclip.copy("")

        keyboard.send("ctrl+c")

        text = ""

        for _ in range(retries):

            time.sleep(delay)

            text = pyperclip.paste()

            if text:
                break

        return text

    def replace_selected_text(self, text):

        pyperclip.copy(text)

        keyboard.send("ctrl+v")

        time.sleep(0.1)

        pyperclip.copy(self.previous_clipboard)