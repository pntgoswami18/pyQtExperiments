"""Trying Main-window style application with PyQt"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar


class Window(QMainWindow):
    """Main-Window

    Arguments:
        QMainWindow {QMainWindow} -- Main Window constructor
    """

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Main-window Application')
        self.setCentralWidget(QLabel('The Central Widget'))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
