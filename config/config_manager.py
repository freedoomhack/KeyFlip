import sys
import json
from pathlib import Path


class ConfigManager:

    DEFAULT = {
        "hotkey": "ctrl+shift+m",
        "startup": False,
        "notification": True,
        "theme": "system"
    }

    def __init__(self):

        if getattr(sys, "frozen", False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).parent

        self.config_path = base_dir / "settings.json"

        self.settings = {}

        self.load()

    def load(self):

        if not self.config_path.exists():

            self.settings = self.DEFAULT.copy()

            self.save()

            return

        try:

            with open(self.config_path, "r", encoding="utf-8") as f:

                self.settings = json.load(f)

        except:

            self.settings = self.DEFAULT.copy()

            self.save()

    def save(self):

        with open(self.config_path, "w", encoding="utf-8") as f:

            json.dump(
                self.settings,
                f,
                indent=4,
                ensure_ascii=False
            )

    def get(self, key, default=None):

        return self.settings.get(key, default)

    def set(self, key, value):

        self.settings[key] = value

        self.save()