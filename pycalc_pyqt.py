#!/usr/bin/env python3
"""Trying to build a calculator with MVC implemented through PyQt5"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from functools import partial

ERROR_MSG = 'ERROR'

__version__ = '0.1'
__author__ = 'Punit Goswami'


class PyCalcUi(QMainWindow):
    """Defines the skeleton UI for the Calculator

    Arguments:
        QMainWindow {QMainWindow} -- subclasses QMainWindow
    """

    def _createDisplay(self):
        """Creates the display for Calc
        """
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        self.layout.addWidget(self.display)

    def _createButtons(self):
        """Creates calc buttons
        """
        self.buttons = {}
        buttonsLayout = QGridLayout()

        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),
                   }

        for btnTxt, pos in buttons.items():
            self.buttons[btnTxt] = QPushButton(btnTxt)
            self.buttons[btnTxt].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btnTxt], pos[0], pos[1])
        self.layout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        return self.setDisplayText('')

    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('PyQt Calculator Application')
        self.setFixedSize(235, 235)
        self.layout = QVBoxLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.layout)
        self._createDisplay()
        self._createButtons()


class PyCalcController:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self. _connectSignals()

    def _calculateResult(self):
        """Evaluate expressions"""
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)


def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


def main():
    """Main method for the calculator
    """
    pycalcApp = QApplication(sys.argv)
    pycalcView = PyCalcUi()
    pycalcView.show()
    model = evaluateExpression
    PyCalcController(model=model, view=pycalcView)
    sys.exit(pycalcApp.exec())


if __name__ == '__main__':
    main()
