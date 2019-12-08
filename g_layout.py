"""Trying out the Grid Layout with PyQt5"""

import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Grid Layout Example')
layout = QGridLayout()

layout.addWidget(QPushButton('Button 1'), 0, 0)
layout.addWidget(QPushButton('Button 2'), 0, 1)
layout.addWidget(QPushButton('Button 3'), 0, 2)
layout.addWidget(QPushButton('Button 4'), 1, 1)
# positional arguments (button, gridRow, gridColumn, rowSpan, columnSpan)
layout.addWidget(QPushButton('Button 5'), 2, 0,1,3)

window.setLayout(layout)
window.show()
sys.exit(app.exec())