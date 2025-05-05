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

        # Objetos para trabalhar
        self.local_service.add_local("Alameda do ferro", "Jose")
        self.local_service.add_local("Avenida stuart litle", "Raimundo")

        self.tool_service.add_tool("0101", "Furadeira", "110v", "Dewalt", "zc1000", "Funcionando")
        self.tool_service.add_tool("2501", "Maquina de solda", "220v", "Arcweld", "Box1000", "Funcionando")
        self.tool_service.add_tool("0110", "Esmerilhadeira", "110v", "Bosch", "b490", "Com defeito")


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

    # Tools Functions
    def load_table_tools(self):
        # load table widget tools
        self.ToolsTableWidget.clear()
        self.ToolsTableWidget.setColumnCount(len(self.tool_repository.atributos))
        self.ToolsTableWidget.setRowCount(len(self.tool_service.get_tools()))
        self.ToolsTableWidget.setHorizontalHeaderLabels(self.tool_repository.atributos)
        for i,item in enumerate(self.tool_service.get_tools()):
            self.ToolsTableWidget.setItem(i,0,QTableWidgetItem(item.id))
            self.ToolsTableWidget.setItem(i,1,QTableWidgetItem(item.tipo))
            self.ToolsTableWidget.setItem(i,2,QTableWidgetItem(item.tensao))
            self.ToolsTableWidget.setItem(i,3,QTableWidgetItem(item.marca))
            self.ToolsTableWidget.setItem(i,4,QTableWidgetItem(item.modelo))
            self.ToolsTableWidget.setItem(i,5,QTableWidgetItem(item.condicao))


    # Dialog Tool Functions
    def show_dialog_tool_add_mode(self):
        self.dialog_tool.ButtonDialogToolExcluir.setDisabled(True)
        self.dialog_tool.show()
    
    def save_data_dialog_tool(self):
        data = self.dialog_tool.get_inputs()
        self.tool_service.add_tool(data[0], data[1], data[2], data[3], data[4], data[5])
        self.dialog_tool.clear_inputs()
        self.load_table_tools()
        self.dialog_tool.close()


    # Dialog Local Functions
    def show_dialog_local_add_mode(self):
        self.dialog_local.show()
    
    def save_data_dialog_local(self):
        data = self.dialog_local.get_inputs()
        self.local_service.add_local(data[0], data[1])
        self.dialog_local.clear_inputs()

        print(self.local_service.get_locals())
    
        # Menu Functions
    def open_home_page(self):
        self.BodyWidget.setCurrentIndex(0)
    
    def open_local_page(self):
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
