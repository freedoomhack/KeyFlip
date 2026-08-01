import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QStyle
from PySide6.QtGui import QIcon


class TrayService:

    def __init__(self, window, quit_callback):

        self.window = window

        icon = self._load_icon()

        self.tray_icon = QSystemTrayIcon(icon)

        self.tray_icon.setToolTip("KeyFlip")

        menu = QMenu()

        open_action = menu.addAction("Open Settings")
        open_action.triggered.connect(self.show_window)

        quit_action = menu.addAction("Exit")
        quit_action.triggered.connect(quit_callback)

        self.tray_icon.setContextMenu(menu)

        self.tray_icon.activated.connect(self.on_activated)

        self.tray_icon.show()

    def _load_icon(self):

        if getattr(sys, "frozen", False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).parent.parent

        icon_path = base_dir / "assets" / "icon.ico"

        if icon_path.exists():
            return QIcon(str(icon_path))

        return QApplication.instance().style().standardIcon(
            QStyle.StandardPixmap.SP_ComputerIcon
        )

    def show_window(self):

        self.window.showNormal()

        self.window.activateWindow()

    def on_activated(self, reason):

        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.show_window()