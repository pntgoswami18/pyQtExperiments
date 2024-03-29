"""Simple hello world Program with PyQt5"""
import sys

# 1. Import `QApplication` and all the required widgets
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


# 2. Create an instance of QApplication
app = QApplication(sys.argv)

# 3. Create an instance of your application's GUI
window = QWidget()
window.setWindowTitle('PyQt5: Hello World')
window.setGeometry(100, 100, 280, 80)
window.move(600, 150)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop (or main loop)
sys.exit(app.exec())
