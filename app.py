import sys
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidget, QTableWidgetItem
from PySide6 import QtWidgets

from controller.tool_service import ToolService
from repository.tool_repository import ToolRepository

from controller.local_service import LocalService
from repository.local_repository import LocalRepository

from views.main_window_ui import Ui_MainWindow
from views.dialog_tool_ui import Ui_DialogTool
from views.dialog_local_ui import Ui_DialogLocal


# Main class initialize window
class Main_Window(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.dialog_tool = DialogTool()
        self.dialog_local = DialogLocal()

        self.tool_repository = ToolRepository()
        self.tool_service = ToolService(self.tool_repository)

        self.local_repository = LocalRepository()
        self.local_service = LocalService(self.local_repository)

        # Preload
        self.BodyWidget.setCurrentIndex(0)
        #self.load_table_locals()
        #self.load_table_tools()
        #self.load_all_combobox()

        # tools page connections
        self.ButtonAdicionarTools.clicked.connect(self.show_dialog_tool_add_mode)

        # dialog tools conections
        self.dialog_tool.ButtonDialogToolFinalizar.clicked.connect(self.save_data_dialog_tool)

        # local page connections
        self.ButtonAdicionarLocals.clicked.connect(self.show_dialog_local_add_mode)

        # dialog local connections
        self.dialog_local.ButtonDialogLocalFinalizar.clicked.connect(self.save_data_dialog_local)

        # Linking menu functions
        self.ButtonInicio.clicked.connect(self.open_home_page)
        self.ButtonLocais.clicked.connect(self.open_local_page)
        self.ButtonFerramentas.clicked.connect(self.open_tools_page)

        # Testes
        self.ToolsTableWidget.itemDoubleClicked.connect(self.toolduploclique)
        self.LocalsTableWidget.itemDoubleClicked.connect(self.localduploclique)

    def toolduploclique(self):
        linha = self.ToolsTableWidget.currentRow()
        coluna = self.ToolsTableWidget.currentColumn()
        print(self.ToolsTableWidget.item(linha, 0).text())
    
    def localduploclique(self):
        linha = self.LocalsTableWidget.currentRow()
        coluna = self.LocalsTableWidget.currentColumn()
        print(self.LocalsTableWidget.item(linha, 0).text())

    # Load Tables
    def load_table_tools(self):
        # load table widget tools
        self.ToolsTableWidget.clear()
        self.ToolsTableWidget.setColumnCount(len(ToolRepository.atributos))
        self.ToolsTableWidget.setHorizontalHeaderLabels(ToolRepository.atributos)
        self.ToolsTableWidget.setRowCount(len(self.tool_service.get_tools()))
        for i,item in enumerate(self.tool_service.get_tools()):
            self.ToolsTableWidget.setItem(i,0,QTableWidgetItem(str(item.id)))
            self.ToolsTableWidget.setItem(i,1,QTableWidgetItem(item.tipo))
            self.ToolsTableWidget.setItem(i,2,QTableWidgetItem(item.tensao))
            self.ToolsTableWidget.setItem(i,3,QTableWidgetItem(item.marca))
            self.ToolsTableWidget.setItem(i,4,QTableWidgetItem(item.modelo))
            self.ToolsTableWidget.setItem(i,5,QTableWidgetItem(item.condicao))
    
    def load_table_locals(self):
        self.LocalsTableWidget.clear()
        self.LocalsTableWidget.setColumnCount(len(LocalRepository.atributos))
        self.LocalsTableWidget.setHorizontalHeaderLabels(LocalRepository.atributos)
        self.LocalsTableWidget.setRowCount(len(self.local_service.get_locals()))
        for i, item in enumerate(self.local_service.get_locals()):
            self.LocalsTableWidget.setItem(i, 0, QTableWidgetItem(str(item.id)))
            self.LocalsTableWidget.setItem(i, 1, QTableWidgetItem(item.nome))
            self.LocalsTableWidget.setItem(i, 2, QTableWidgetItem(item.responsavel))

    def load_all_combobox(self):
        for i in self.local_repository.locals:
            self.dialog_tool.ComboBoxToolLocal.addItem(i.nome)
        for i in self.tool_repository.tools:
            self.dialog_tool.ComboBoxToolTipo.addItem(i.tipo)
            self.dialog_tool.ComboboxToolMarca.addItem(i.marca)

    # Dialog Tool Functions
    def show_dialog_tool_add_mode(self):
        self.dialog_tool.ButtonDialogToolExcluir.setDisabled(True)
        self.dialog_tool.show()
    
    def save_data_dialog_tool(self):
        data = self.dialog_tool.get_inputs()
        self.tool_service.add_tool(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        self.dialog_tool.clear_inputs()
        self.load_table_tools()
        self.dialog_tool.close()

    # Dialog Local Functions
    def show_dialog_local_add_mode(self):
        self.dialog_local.show()
    
    def save_data_dialog_local(self):
        data = self.dialog_local.get_inputs()
        self.dialog_local.clear_inputs()
        self.local_service.add_local(data[0], data[1])
        self.load_table_locals()
        self.dialog_local.close()

        # Menu Functions
    def open_home_page(self):
        self.BodyWidget.setCurrentIndex(0)
    
    def open_local_page(self):
        self.load_table_locals()
        self.BodyWidget.setCurrentIndex(1)

    def open_tools_page(self):
        self.load_table_tools()
        self.BodyWidget.setCurrentIndex(2)
    
    def open_view_local(self):
        self.BodyWidget.setCurrentIndex(3)


# Initialize dialog tool window
class DialogTool(QDialog, Ui_DialogTool):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    


# Initialize dialog local window
class DialogLocal(QDialog, Ui_DialogLocal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    sys.exit(app.exec())
