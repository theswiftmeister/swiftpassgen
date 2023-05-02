from PyQt6 import QtCore,QtGui
from PyQt6.QtWidgets import QMainWindow 
from uipy import MainWindowUi
from .addpassdialog import AddPasswordDialog
from .viewpassworddialog import ViewPasswordDialog
from .passwordgenerator import *
from .fileio import FileIO


DOCUMENTS_DIRECTORY = f"./my_pass.sx"



class MainWindow(QMainWindow, MainWindowUi):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.pushButton_save_passwords.setShortcut(QtGui.QKeySequence("Ctrl+S"))

        self.show_pass_dialog = ViewPasswordDialog(self)
        self.pass_dialog = AddPasswordDialog(self)
        self.my_fileio = FileIO()
        try:
            self.password_dict = self.my_fileio.load("./my_pass.sx")
        except:
            self.password_dict = {}

        self.pushButton_show_saved_passwords.clicked.connect(self.show_all_passwords)
        self.pushButton_generate_password.clicked.connect(self.generate_password)
        self.pushButton_save_generated_password.clicked.connect(lambda : self.open_generated_password_dialog(self.pass_dialog))
        self.pushButton_save_my_password.clicked.connect(lambda : self.open_my_password_dialog(self.pass_dialog))
        self.pushButton_save_passwords.clicked.connect(self.save_passwords_to_txt)
    
    def show_all_passwords(self):
        if self.password_dict == {}:
            self.statusbar.showMessage("Password table is empty...",3000)
            return

        items = self.show_pass_dialog.tableWidget.rowCount()

        for i in range(items,len(self.password_dict.keys())):
            key = list(self.password_dict.keys())[i]
            value = self.password_dict[key]
            self.show_pass_dialog.add_row(key,value)
            # print("inserted..." ,value )

        self.show_pass_dialog.show()

    def open_generated_password_dialog(self,dialog:AddPasswordDialog):
        generated_passowrd = self.lineEdit_generated_password.text()
        if not generated_passowrd:
            self.statusbar.showMessage("Generated password empty...",3000)
            return

        dialog.set_password_lineedit(True,generated_passowrd)
        dialog.add_generate_password()
        dialog.show()
    
    def open_my_password_dialog(self,dialog:AddPasswordDialog):
        dialog.add_custom_password()
        dialog.show()

    def generate_password(self):
        length = int(self.spinBox_password_length.text())
        has_symbols = self.checkBox_symbols.isChecked()
        has_numbers = self.checkBox_numbers.isChecked()
        has_lowercase = self.checkBox_lowercase_char.isChecked()
        has_uppercase = self.checkBox_uppercase_char.isChecked()
        has_repeated_char = self.checkBox_repeated_char.isChecked()
        has_ambiguous_char = self.checkBox_ambiguous_char.isChecked()
        try:
            password = generate_password(length,has_symbols,has_numbers,has_lowercase,has_uppercase,has_repeated_char,has_ambiguous_char)
            self.lineEdit_generated_password.setText(password)
        except NoOptionSelected:
            self.statusbar.showMessage("Please select atleast one parameter...",3000)
            return
        except NotEnoughCharacters:
            self.statusbar.showMessage("Not enough characters to generate password..",3000)
            return
    
    def add_saved_passwords(self,site:str,id:str,password:str):
        key = site
        value = {"id":id, "pass" : password}
        self.password_dict[key] = value
        self.lineEdit_generated_password.clear()
        if self.show_pass_dialog.isVisible():
            self.show_pass_dialog.add_row(key,value)
            self.show_pass_dialog.update()
        # self.show_dic()
    
    def remove_saved_password(self,key):
        self.password_dict.pop(key)
        # self.show_dic()
    
    def save_passwords_to_txt(self):
        self.my_fileio.save("./my_pass.sx",self.password_dict)
        self.statusbar.showMessage("Passwords saved to my_pass.sx...",3000)

    def show_dic(self):
        print(self.password_dict,sep="\n")







    



    
