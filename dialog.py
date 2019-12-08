"""Trying the Dialog-style application with PyQt"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QVBoxLayout


class Dialog(QDialog):
    """Dialog

    Arguments:
        QDialog {QDialog} -- QDialog Constructor for a dialog
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Dialog Example')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name', QLineEdit())
        formLayout.addRow('Age', QLineEdit())
        formLayout.addRow('Job', QLineEdit())
        formLayout.addRow('Hobbies', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec())
