import sys
import logging
from pathlib import Path


class Logger:

    def __init__(self):

        if getattr(sys, "frozen", False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).parent.parent

        log_dir = base_dir / "logs"

        log_dir.mkdir(exist_ok=True)

        logging.basicConfig(
            filename=str(log_dir / "keyflip.log"),
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

    def info(self, message):

        logging.info(message)

    def error(self, message):

        logging.error(message)