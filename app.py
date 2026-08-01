from core.converter import Converter
from services.clipboard_service import ClipboardService
from services.hotkey_service import HotkeyService
from services.startup_service import StartupService
from config.config_manager import ConfigManager
from services.logger import Logger


class KeyFlipApp:

    def __init__(self):

        self.logger = Logger()
        self.config = ConfigManager()

        self.converter = Converter()
        self.clipboard = ClipboardService()

        self.hotkey = HotkeyService(self.convert_selected_text)

        self.startup = StartupService()

    def convert_selected_text(self):

        self.logger.info("Hotkey Pressed")

        text = self.clipboard.get_selected_text()

        if not text:
            self.logger.info("No Text Selected")
            return

        self.logger.info(f"Selected : {text}")

        converted = self.converter.convert(text)

        self.logger.info(f"Converted : {converted}")

        self.clipboard.replace_selected_text(converted)

        self.logger.info("Finished")

    def run(self):

        hotkey = self.config.get("hotkey", "ctrl+shift+m")

        self.logger.info(f"Hotkey = {hotkey}")

        print("===================================")
        print("          KeyFlip Running")
        print("===================================")
        print(f"Shortcut : {hotkey}")
        print()

        self.hotkey.start(hotkey)

        if self.config.get("startup", False):
            self.startup.enable()
        else:
            self.startup.disable()

    def update_hotkey(self, new_hotkey):

        self.logger.info(f"Hotkey Updated -> {new_hotkey}")

        self.hotkey.update(new_hotkey)

    def update_startup(self, enabled):

        self.logger.info(f"Startup Updated -> {enabled}")

        if enabled:
            self.startup.enable()
        else:
            self.startup.disable()