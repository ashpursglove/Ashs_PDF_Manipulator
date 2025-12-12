"""
main.py

Entry point for "Ash's PDF Manipulator".

Creates the QApplication and shows the main window.
"""

import sys
from PyQt5 import QtWidgets

from modules.gui import PdfManipulatorWindow  # type: ignore
from modules.theme import DARK_BLUE_ORANGE_QSS  # type: ignore


def main() -> None:
    """
    Main entry point: create the QApplication, apply theme, and show the main window.
    """
    app = QtWidgets.QApplication(sys.argv)

    # Apply the dark blue + orange stylesheet to the whole app
    app.setStyleSheet(DARK_BLUE_ORANGE_QSS)

    window = PdfManipulatorWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
