# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_local.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_DialogLocal(object):
    def setupUi(self, DialogLocal):
        if not DialogLocal.objectName():
            DialogLocal.setObjectName(u"DialogLocal")
        DialogLocal.resize(660, 145)
        DialogLocal.setMinimumSize(QSize(660, 0))
        DialogLocal.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout = QVBoxLayout(DialogLocal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 10)
        self.DialogLocalBodyWidget = QFrame(DialogLocal)
        self.DialogLocalBodyWidget.setObjectName(u"DialogLocalBodyWidget")
        self.DialogLocalBodyWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.DialogLocalBodyWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.DialogLocalBodyWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LabelLocalAction = QLabel(self.DialogLocalBodyWidget)
        self.LabelLocalAction.setObjectName(u"LabelLocalAction")
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(16)
        self.LabelLocalAction.setFont(font)
        self.LabelLocalAction.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.LabelLocalAction)

        self.labeldialoglocal = QLabel(self.DialogLocalBodyWidget)
        self.labeldialoglocal.setObjectName(u"labeldialoglocal")
        self.labeldialoglocal.setFont(font)

        self.horizontalLayout.addWidget(self.labeldialoglocal)


        self.verticalLayout.addWidget(self.DialogLocalBodyWidget, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(DialogLocal)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(65, 0))
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label)

        self.TextInputLocalNome = QLineEdit(self.frame_3)
        self.TextInputLocalNome.setObjectName(u"TextInputLocalNome")

        self.horizontalLayout_5.addWidget(self.TextInputLocalNome)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.TextInputLocalResponsavel = QLineEdit(self.frame)
        self.TextInputLocalResponsavel.setObjectName(u"TextInputLocalResponsavel")

        self.horizontalLayout_4.addWidget(self.TextInputLocalResponsavel)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_2)

        self.DialogLocalButtonNav = QFrame(DialogLocal)
        self.DialogLocalButtonNav.setObjectName(u"DialogLocalButtonNav")
        self.DialogLocalButtonNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.DialogLocalButtonNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.DialogLocalButtonNav)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ButtonDialogLocalExcluir = QPushButton(self.DialogLocalButtonNav)
        self.ButtonDialogLocalExcluir.setObjectName(u"ButtonDialogLocalExcluir")

        self.horizontalLayout_2.addWidget(self.ButtonDialogLocalExcluir)

        self.ButtonDialogLocalCancelar = QPushButton(self.DialogLocalButtonNav)
        self.ButtonDialogLocalCancelar.setObjectName(u"ButtonDialogLocalCancelar")

        self.horizontalLayout_2.addWidget(self.ButtonDialogLocalCancelar)

        self.ButtonDialogLocalFinalizar = QPushButton(self.DialogLocalButtonNav)
        self.ButtonDialogLocalFinalizar.setObjectName(u"ButtonDialogLocalFinalizar")

        self.horizontalLayout_2.addWidget(self.ButtonDialogLocalFinalizar)


        self.verticalLayout.addWidget(self.DialogLocalButtonNav, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)
        
        # Linking nav buttons
        self.ButtonDialogLocalCancelar.clicked.connect(self.close_dialog)


        self.retranslateUi(DialogLocal)

        QMetaObject.connectSlotsByName(DialogLocal)

    # System Functions
    def clear_inputs(self):
        self.TextInputLocalNome.setText("")
        self.TextInputLocalResponsavel.setText("")
    
    def get_inputs(self):
        nome = str(self.TextInputLocalNome.text()).lower()
        responsavel = str(self.TextInputLocalResponsavel.text()).lower()
        data = (nome, responsavel)
        return data

    def close_dialog(self):
        self.clear_inputs()
        self.close()

    # setupUi

    def retranslateUi(self, DialogLocal):
        DialogLocal.setWindowTitle(QCoreApplication.translate("DialogLocal", u"Dialog", None))
        self.LabelLocalAction.setText(QCoreApplication.translate("DialogLocal", u"Adicionando", None))
        self.labeldialoglocal.setText(QCoreApplication.translate("DialogLocal", u"Local", None))
        self.label.setText(QCoreApplication.translate("DialogLocal", u"Nome", None))
        self.label_2.setText(QCoreApplication.translate("DialogLocal", u"Responsavel", None))
        self.ButtonDialogLocalExcluir.setText(QCoreApplication.translate("DialogLocal", u"Excluir", None))
        self.ButtonDialogLocalCancelar.setText(QCoreApplication.translate("DialogLocal", u"Cancelar", None))
        self.ButtonDialogLocalFinalizar.setText(QCoreApplication.translate("DialogLocal", u"Finalizar", None))
    # retranslateUi

