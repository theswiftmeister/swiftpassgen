# uipy/__init__.py
from .mainwindow import MainWindowUi
from .addpassdialog import AddPasswordDialog
from .passwordsdialog import ViewPasswordsDialog
import os


# App icons
file_path = os.path.dirname(os.path.abspath(__file__))
MAIN_ICON = f'{file_path}\\..\\graphics\\1.png'
SAVE_ICON = f'{file_path}\\..\\graphics\\2.jpg'