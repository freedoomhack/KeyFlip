import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from app import KeyFlipApp
from gui.settings_window import SettingsWindow
from services.tray_service import TrayService


def resolve_icon_path():

    if getattr(sys, "frozen", False):
        base_dir = Path(sys.executable).parent
    else:
        base_dir = Path(__file__).parent

    return base_dir / "assets" / "icon.ico"


def main():

    keyflip = KeyFlipApp()

    keyflip.run()

    qt_app = QApplication(sys.argv)

    qt_app.setQuitOnLastWindowClosed(False)

    icon_path = resolve_icon_path()

    if icon_path.exists():
        app_icon = QIcon(str(icon_path))
        qt_app.setWindowIcon(app_icon)

    window = SettingsWindow(keyflip)

    if icon_path.exists():
        window.setWindowIcon(app_icon)

    tray = TrayService(window, qt_app.quit)

    window.show()

    sys.exit(qt_app.exec())


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)