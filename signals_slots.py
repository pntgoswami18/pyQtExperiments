"""Trying signals and slots mechanism in PyQt5"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


def getGreeting():
    """Returns a greeting string
    """
    if msg.text():
        msg.setText('')
    else:
        msg.setText("Hello there!")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals-Slots Application')
layout = QVBoxLayout()
btn = QPushButton('Get a greeting')

# usual pattern for signal slot connection is
# widget.signal.connect(slot_function)
btn.clicked.connect(getGreeting)

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())
