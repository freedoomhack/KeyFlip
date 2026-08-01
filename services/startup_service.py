import sys
import winreg


class StartupService:

    REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
    APP_NAME = "KeyFlip"

    def enable(self):

        exe_path = sys.executable

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            self.REG_PATH,
            0,
            winreg.KEY_SET_VALUE
        )

        winreg.SetValueEx(
            key,
            self.APP_NAME,
            0,
            winreg.REG_SZ,
            exe_path
        )

        winreg.CloseKey(key)

    def disable(self):

        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                self.REG_PATH,
                0,
                winreg.KEY_SET_VALUE
            )

            winreg.DeleteValue(key, self.APP_NAME)

            winreg.CloseKey(key)

        except FileNotFoundError:
            pass

    def is_enabled(self):

        try:
            key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER,
                self.REG_PATH,
                0,
                winreg.KEY_READ
            )

            winreg.QueryValueEx(key, self.APP_NAME)

            winreg.CloseKey(key)

            return True

        except FileNotFoundError:
            return False