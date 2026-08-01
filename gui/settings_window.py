from config.config_manager import ConfigManager
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QLineEdit,
)

from gui.style import STYLE


class SettingsWindow(QWidget):

    def __init__(self, app):

        super().__init__()

        self.app = app

        self.config = ConfigManager()

        self.setWindowTitle("KeyFlip")

        self.resize(420,300)

        self.setStyleSheet(STYLE)

        self.build_ui()

        self.load_settings()

    def build_ui(self):

        layout=QVBoxLayout()

        title=QLabel("KeyFlip")

        title.setStyleSheet("font-size:22px;font-weight:bold;")

        layout.addWidget(title)

        layout.addSpacing(15)

        hotkeyLayout=QHBoxLayout()

        hotkeyLayout.addWidget(QLabel("Shortcut"))

        self.hotkeyEdit=QLineEdit()

        self.hotkeyEdit.setText("Ctrl+Shift+M")

        hotkeyLayout.addWidget(self.hotkeyEdit)

        layout.addLayout(hotkeyLayout)

        layout.addSpacing(15)

        self.startup=QCheckBox("Run at Windows Startup")

        layout.addWidget(self.startup)

        self.notify=QCheckBox("Enable Notification")

        layout.addWidget(self.notify)

        layout.addStretch()

        self.saveButton=QPushButton("Save")

        self.saveButton.clicked.connect(self.save_settings)

        layout.addWidget(self.saveButton)

        self.setLayout(layout)

    def load_settings(self):

        self.hotkeyEdit.setText(
            self.config.get("hotkey", "ctrl+shift+m")
        )

        self.startup.setChecked(
            self.config.get("startup", False)
        )

        self.notify.setChecked(
            self.config.get("notification", True)
        )

    def save_settings(self):

        new_hotkey = self.hotkeyEdit.text().lower()

        self.config.set("hotkey", new_hotkey)

        self.config.set(
            "startup",
            self.startup.isChecked()
        )

        self.config.set(
            "notification",
            self.notify.isChecked()
        )

        self.app.update_hotkey(new_hotkey)

        self.app.update_startup(self.startup.isChecked())

        print("Settings Saved")

    def closeEvent(self, event):

        event.ignore()

        self.hide()