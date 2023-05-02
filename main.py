# venv\scripts\activate

from PyQt6.QtWidgets import QApplication,QMainWindow
from modules import MainWindow

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main:QMainWindow = MainWindow()
    main.show()
    sys.exit(app.exec())