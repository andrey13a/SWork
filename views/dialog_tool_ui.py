# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_tool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_DialogTool(object):
    def setupUi(self, DialogTool):
        if not DialogTool.objectName():
            DialogTool.setObjectName(u"DialogTool")
        DialogTool.resize(660, 259)
        DialogTool.setMinimumSize(QSize(660, 250))
        self.verticalLayout = QVBoxLayout(DialogTool)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DialogBodyWidget = QStackedWidget(DialogTool)
        self.DialogBodyWidget.setObjectName(u"DialogBodyWidget")
        self.DialogToolPage = QWidget()
        self.DialogToolPage.setObjectName(u"DialogToolPage")
        self.verticalLayout_2 = QVBoxLayout(self.DialogToolPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.DialogToolPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.LabelToolAction = QLabel(self.frame_2)
        self.LabelToolAction.setObjectName(u"LabelToolAction")
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(16)
        self.LabelToolAction.setFont(font)
        self.LabelToolAction.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.LabelToolAction)

        self.logodialogtool = QLabel(self.frame_2)
        self.logodialogtool.setObjectName(u"logodialogtool")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logodialogtool.sizePolicy().hasHeightForWidth())
        self.logodialogtool.setSizePolicy(sizePolicy)
        self.logodialogtool.setFont(font)
        self.logodialogtool.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.logodialogtool)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.DialogToolPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_16)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))
        self.label.setMaximumSize(QSize(60, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label)

        self.TextInputIdTool = QLineEdit(self.frame_16)
        self.TextInputIdTool.setObjectName(u"TextInputIdTool")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TextInputIdTool.sizePolicy().hasHeightForWidth())
        self.TextInputIdTool.setSizePolicy(sizePolicy1)
        self.TextInputIdTool.setMinimumSize(QSize(50, 0))
        self.TextInputIdTool.setMaximumSize(QSize(50, 16777215))
        self.TextInputIdTool.setMaxLength(4)

        self.horizontalLayout_6.addWidget(self.TextInputIdTool)

        self.CheckBoxAutoId = QCheckBox(self.frame_16)
        self.CheckBoxAutoId.setObjectName(u"CheckBoxAutoId")

        self.horizontalLayout_6.addWidget(self.CheckBoxAutoId)


        self.horizontalLayout_4.addWidget(self.frame_16, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_15 = QFrame(self.frame_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_4.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.DialogToolPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setMaximumSize(QSize(60, 16777215))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.ComboBoxToolTipo = QComboBox(self.frame_7)
        self.ComboBoxToolTipo.setObjectName(u"ComboBoxToolTipo")
        self.ComboBoxToolTipo.setMinimumSize(QSize(150, 0))
        self.ComboBoxToolTipo.setMaximumSize(QSize(150, 16777215))
        self.ComboBoxToolTipo.setEditable(True)

        self.horizontalLayout_7.addWidget(self.ComboBoxToolTipo)


        self.horizontalLayout_3.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.ComboBoxToolTensao = QComboBox(self.frame_8)
        self.ComboBoxToolTensao.setObjectName(u"ComboBoxToolTensao")
        self.ComboBoxToolTensao.setMinimumSize(QSize(50, 0))
        self.ComboBoxToolTensao.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.ComboBoxToolTensao)


        self.horizontalLayout_3.addWidget(self.frame_8, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.DialogToolPage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 0))
        self.label_7.setMaximumSize(QSize(60, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.ComboboxToolMarca = QComboBox(self.frame_12)
        self.ComboboxToolMarca.setObjectName(u"ComboboxToolMarca")
        self.ComboboxToolMarca.setMinimumSize(QSize(150, 0))
        self.ComboboxToolMarca.setMaximumSize(QSize(150, 16777215))
        self.ComboboxToolMarca.setEditable(True)

        self.horizontalLayout_10.addWidget(self.ComboboxToolMarca)


        self.horizontalLayout_2.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))
        self.label_4.setMaximumSize(QSize(60, 16777215))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.TextInputToolModelo = QLineEdit(self.frame_11)
        self.TextInputToolModelo.setObjectName(u"TextInputToolModelo")
        sizePolicy1.setHeightForWidth(self.TextInputToolModelo.sizePolicy().hasHeightForWidth())
        self.TextInputToolModelo.setSizePolicy(sizePolicy1)
        self.TextInputToolModelo.setMinimumSize(QSize(250, 0))
        self.TextInputToolModelo.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_9.addWidget(self.TextInputToolModelo)


        self.horizontalLayout_2.addWidget(self.frame_11, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame = QFrame(self.DialogToolPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 0))
        self.label_6.setMaximumSize(QSize(60, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.ComboBoxToolCondicao = QComboBox(self.frame_9)
        self.ComboBoxToolCondicao.setObjectName(u"ComboBoxToolCondicao")
        self.ComboBoxToolCondicao.setMinimumSize(QSize(150, 0))
        self.ComboBoxToolCondicao.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_11.addWidget(self.ComboBoxToolCondicao)


        self.horizontalLayout.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMaximumSize(QSize(60, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.ComboBoxToolLocal = QComboBox(self.frame_10)
        self.ComboBoxToolLocal.setObjectName(u"ComboBoxToolLocal")
        self.ComboBoxToolLocal.setMinimumSize(QSize(250, 0))
        self.ComboBoxToolLocal.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_12.addWidget(self.ComboBoxToolLocal)


        self.horizontalLayout.addWidget(self.frame_10, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame)

        self.DialogButtonNav = QFrame(self.DialogToolPage)
        self.DialogButtonNav.setObjectName(u"DialogButtonNav")
        self.DialogButtonNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.DialogButtonNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.DialogButtonNav)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ButtonDialogToolExcluir = QPushButton(self.DialogButtonNav)
        self.ButtonDialogToolExcluir.setObjectName(u"ButtonDialogToolExcluir")
        self.ButtonDialogToolExcluir.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.ButtonDialogToolExcluir)

        self.ButtonDialogToolCancelar = QPushButton(self.DialogButtonNav)
        self.ButtonDialogToolCancelar.setObjectName(u"ButtonDialogToolCancelar")

        self.horizontalLayout_5.addWidget(self.ButtonDialogToolCancelar)

        self.ButtonDialogToolFinalizar = QPushButton(self.DialogButtonNav)
        self.ButtonDialogToolFinalizar.setObjectName(u"ButtonDialogToolFinalizar")

        self.horizontalLayout_5.addWidget(self.ButtonDialogToolFinalizar)


        self.verticalLayout_2.addWidget(self.DialogButtonNav, 0, Qt.AlignmentFlag.AlignRight)

        self.DialogBodyWidget.addWidget(self.DialogToolPage)

        self.verticalLayout.addWidget(self.DialogBodyWidget)

        self.DialogBodyWidget.setCurrentIndex(0)

        self.retranslateUi(DialogTool)

        QMetaObject.connectSlotsByName(DialogTool)

        # Button Conections
        self.ButtonDialogToolCancelar.clicked.connect(self.close_dialog)
    
    # System Function
    def clear_inputs(self):
        self.TextInputIdTool.setText("")
        self.ComboBoxToolTipo.setEditText("")
        self.ComboBoxToolTensao.setEditText("")
        self.ComboboxToolMarca.setEditText("")
        self.TextInputToolModelo.setText("")
        self.ComboBoxToolCondicao.setEditText("")
    
    def get_inputs(self):
        id = str(self.TextInputIdTool.text()).lower()
        tipo = str(self.ComboBoxToolTipo.currentText()).lower()
        tensao = str(self.ComboBoxToolTensao.currentText()).lower()
        marca = str(self.ComboboxToolMarca.currentText()).lower()
        modelo = str(self.TextInputToolModelo.text()).lower()
        condicao = str(self.ComboBoxToolCondicao.currentText()).lower()

        data = (id, tipo, tensao, marca, modelo, condicao)
        return data

    def close_dialog(self):
        self.clear_inputs()
        self.close()

    # setupUi

    def retranslateUi(self, DialogTool):
        DialogTool.setWindowTitle(QCoreApplication.translate("DialogTool", u"Dialog", None))
        self.LabelToolAction.setText(QCoreApplication.translate("DialogTool", u"Adicionando", None))
        self.logodialogtool.setText(QCoreApplication.translate("DialogTool", u"Ferramenta", None))
        self.label.setText(QCoreApplication.translate("DialogTool", u"Id", None))
        self.CheckBoxAutoId.setText(QCoreApplication.translate("DialogTool", u"Auto", None))
        self.label_2.setText(QCoreApplication.translate("DialogTool", u"Tipo", None))
        self.label_3.setText(QCoreApplication.translate("DialogTool", u"Tens\u00e3o", None))
        self.label_7.setText(QCoreApplication.translate("DialogTool", u"Marca", None))
        self.label_4.setText(QCoreApplication.translate("DialogTool", u"Modelo", None))
        self.label_6.setText(QCoreApplication.translate("DialogTool", u"Condi\u00e7\u00e3o", None))
        self.label_5.setText(QCoreApplication.translate("DialogTool", u"Local", None))
        self.ComboBoxToolCondicao.addItem(QCoreApplication.translate("DialogTool", u"Funcionando", None))
        self.ComboBoxToolCondicao.addItem(QCoreApplication.translate("DialogTool", u"Em manutenção", None))
        self.ComboBoxToolCondicao.addItem(QApplication.translate("DialogTool", u"Com defeito", None))
        self.ComboBoxToolTensao.addItem(QApplication.translate("DialogTool", u"110V", None))
        self.ComboBoxToolTensao.addItem(QApplication.translate("DialogTool", u"220V", None))
        self.ButtonDialogToolExcluir.setText(QCoreApplication.translate("DialogTool", u"Excluir", None))
        self.ButtonDialogToolCancelar.setText(QCoreApplication.translate("DialogTool", u"Cancelar", None))
        self.ButtonDialogToolFinalizar.setText(QCoreApplication.translate("DialogTool", u"Finalizar", None))
    # retranslateUi

