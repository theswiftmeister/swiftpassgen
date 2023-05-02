from PyQt6.QtWidgets import QDialog,QDialogButtonBox
from uipy import AddPasswordDialog

class AddPasswordDialog(QDialog, AddPasswordDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(lambda button : self.button_box_accept(parent,button))
    
    def set_password_lineedit(self,is_read_only:bool,text:str):
        self.lineEdit_password.setReadOnly(is_read_only)
        self.lineEdit_password.setText(text)
    
    def button_box_accept(self,parent,button):
        if self.buttonBox.buttonRole(button) == QDialogButtonBox.ButtonRole.AcceptRole or self.buttonBox.buttonRole(button) == QDialogButtonBox.ButtonRole.ApplyRole:
            site = self.lineEdit_site_name.text().capitalize()
            id = self.lineEdit_password_id.text().capitalize()
            password = self.lineEdit_password.text()
            if not site.strip() or not id.strip() or not password.strip():
                parent.statusbar.showMessage("Field was empty, no password was saved...",3000)
                return
            parent.add_saved_passwords(site,id,password)

        self.clear_line_edit()

    def clear_line_edit(self):
        self.lineEdit_password.clear()
        self.lineEdit_site_name.clear()
        self.lineEdit_password_id.clear()

    def add_generate_password(self):
        self.setWindowTitle("Add generated password")
        self.lineEdit_password.setReadOnly(True)

        self.buttonBox.clear()
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

    def add_custom_password(self):
        self.setWindowTitle("Add my password")
        self.lineEdit_password.setReadOnly(False)
        self.buttonBox.clear()
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Cancel)

    

    