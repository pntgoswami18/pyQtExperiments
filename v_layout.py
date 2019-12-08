"""Trying out the Vertical Layout with PyQt5"""

import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Vertical Layout Example')
layout = QVBoxLayout()

layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Middle'))
layout.addWidget(QPushButton('Bottom'))

window.setLayout(layout)
window.show()
sys.exit(app.exec())