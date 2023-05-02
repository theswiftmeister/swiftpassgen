from PyQt6 import QtCore,QtGui
from PyQt6.QtWidgets import QDialog,QTableWidgetItem,QHeaderView,QApplication
from uipy import ViewPasswordsDialog

class ViewPasswordDialog(QDialog, ViewPasswordsDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        self.this_parent = parent
        self.row_to_delete = None
    
        self.tableWidget.cellDoubleClicked.connect(lambda row,col : self.copy_cell_to_clipboard(row,col))
        self.tableWidget.cellClicked.connect(lambda row,col : self.set_row_to_delete(row,col))

    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Delete and self.row_to_delete != None:
            key = self.tableWidget.item(self.row_to_delete,0).text()
            self.tableWidget.removeRow(self.row_to_delete)
            self.this_parent.remove_saved_password(key)
            self.row_to_delete = None

    def add_row(self,key,value):
        table= self.tableWidget
        table.setRowCount(table.rowCount() + 1)
        row = table.rowCount()

        table.setItem(row-1,0,self.setTableWidgetItem(key))
        table.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeMode.ResizeToContents)
        
        for i,k in enumerate(value.keys()):
            table.setItem(row-1,i+1,self.setTableWidgetItem(value[k]))
            table.horizontalHeader().setSectionResizeMode(i+1,QHeaderView.ResizeMode.ResizeToContents)
    
    def copy_cell_to_clipboard(self,r,c):
        QApplication.clipboard().setText(self.tableWidget.item(r,c).text())
    
    def set_row_to_delete(self,row,col):
        self.row_to_delete = row


    def setTableWidgetItem(self,data) -> QTableWidgetItem:
        item = QTableWidgetItem(str(data))
        item.setFont(self.create_font())
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        return item
    
    def create_font(self):
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setItalic(True)
        font.setWeight(100)
        
        return font

    


