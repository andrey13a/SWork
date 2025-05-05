# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 510)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"#ButtonContato ,  #ButtonSuporte{\n"
"	border: none;\n"
"	color: rgb(0, 0, 255);\n"
"}\n"
"#ButtonContato:hover{\n"
"	color: dodgerblue;\n"
"}\n"
"#ButtonSuporte:hover{\n"
"	color: dodgerblue;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderFrame = QFrame(self.centralwidget)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        self.HeaderFrame.setStyleSheet(u"")
        self.HeaderFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.HeaderFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.HeaderFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.HeaderLeftFrame = QFrame(self.HeaderFrame)
        self.HeaderLeftFrame.setObjectName(u"HeaderLeftFrame")
        self.HeaderLeftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HeaderLeftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.HeaderLeftFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.ButtonInicio = QPushButton(self.HeaderLeftFrame)
        self.ButtonInicio.setObjectName(u"ButtonInicio")

        self.horizontalLayout_2.addWidget(self.ButtonInicio)

        self.ButtonLocais = QPushButton(self.HeaderLeftFrame)
        self.ButtonLocais.setObjectName(u"ButtonLocais")

        self.horizontalLayout_2.addWidget(self.ButtonLocais)

        self.ButtonFerramentas = QPushButton(self.HeaderLeftFrame)
        self.ButtonFerramentas.setObjectName(u"ButtonFerramentas")

        self.horizontalLayout_2.addWidget(self.ButtonFerramentas)


        self.horizontalLayout.addWidget(self.HeaderLeftFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.labelLogo = QLabel(self.HeaderFrame)
        self.labelLogo.setObjectName(u"labelLogo")
        font = QFont()
        font.setFamilies([u"Segoe Print"])
        font.setPointSize(20)
        self.labelLogo.setFont(font)
        self.labelLogo.setStyleSheet(u"")
        self.labelLogo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.labelLogo, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame = QFrame(self.HeaderFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.HeaderFrame)

        self.BodyWidget = QStackedWidget(self.centralwidget)
        self.BodyWidget.setObjectName(u"BodyWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyWidget.sizePolicy().hasHeightForWidth())
        self.BodyWidget.setSizePolicy(sizePolicy)
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.BodyWidget.addWidget(self.HomePage)
        self.LocalsPage = QWidget()
        self.LocalsPage.setObjectName(u"LocalsPage")
        self.verticalLayout_3 = QVBoxLayout(self.LocalsPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.LocalsFrameTop = QFrame(self.LocalsPage)
        self.LocalsFrameTop.setObjectName(u"LocalsFrameTop")
        self.LocalsFrameTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.LocalsFrameTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.LocalsFrameTop)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.LocalsLabelHeader = QLabel(self.LocalsFrameTop)
        self.LocalsLabelHeader.setObjectName(u"LocalsLabelHeader")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setPointSize(16)
        self.LocalsLabelHeader.setFont(font1)
        self.LocalsLabelHeader.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.LocalsLabelHeader, 0, Qt.AlignmentFlag.AlignLeft)

        self.LocalsFilterNav = QFrame(self.LocalsFrameTop)
        self.LocalsFilterNav.setObjectName(u"LocalsFilterNav")
        self.LocalsFilterNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.LocalsFilterNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.LocalsFilterNav)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)

        self.horizontalLayout_9.addWidget(self.LocalsFilterNav)

        self.LocalsButtonsNav = QFrame(self.LocalsFrameTop)
        self.LocalsButtonsNav.setObjectName(u"LocalsButtonsNav")
        self.LocalsButtonsNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.LocalsButtonsNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.LocalsButtonsNav)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ButtonEditarLocals = QPushButton(self.LocalsButtonsNav)
        self.ButtonEditarLocals.setObjectName(u"ButtonEditarLocals")

        self.horizontalLayout_11.addWidget(self.ButtonEditarLocals)

        self.ButtonAdicionarLocals = QPushButton(self.LocalsButtonsNav)
        self.ButtonAdicionarLocals.setObjectName(u"ButtonAdicionarLocals")

        self.horizontalLayout_11.addWidget(self.ButtonAdicionarLocals)


        self.horizontalLayout_9.addWidget(self.LocalsButtonsNav, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.LocalsFrameTop)

        self.LocalsTableWidget = QTableWidget(self.LocalsPage)
        if (self.LocalsTableWidget.columnCount() < 3):
            self.LocalsTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.LocalsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.LocalsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.LocalsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.LocalsTableWidget.setObjectName(u"LocalsTableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LocalsTableWidget.sizePolicy().hasHeightForWidth())
        self.LocalsTableWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.LocalsTableWidget)

        self.BodyWidget.addWidget(self.LocalsPage)
        self.ToolsPage = QWidget()
        self.ToolsPage.setObjectName(u"ToolsPage")
        self.verticalLayout_2 = QVBoxLayout(self.ToolsPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ToolsFrameTop = QFrame(self.ToolsPage)
        self.ToolsFrameTop.setObjectName(u"ToolsFrameTop")
        self.ToolsFrameTop.setMinimumSize(QSize(0, 30))
        self.ToolsFrameTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolsFrameTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ToolsFrameTop)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tools_label_header = QLabel(self.ToolsFrameTop)
        self.tools_label_header.setObjectName(u"tools_label_header")
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.tools_label_header.setFont(font2)

        self.horizontalLayout_6.addWidget(self.tools_label_header, 0, Qt.AlignmentFlag.AlignLeft)

        self.ToolsFilterNav = QFrame(self.ToolsFrameTop)
        self.ToolsFilterNav.setObjectName(u"ToolsFilterNav")
        self.ToolsFilterNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolsFilterNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.ToolsFilterNav)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.toolslabelfiltro = QLabel(self.ToolsFilterNav)
        self.toolslabelfiltro.setObjectName(u"toolslabelfiltro")
        self.toolslabelfiltro.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.toolslabelfiltro)

        self.TextInputFiltro = QLineEdit(self.ToolsFilterNav)
        self.TextInputFiltro.setObjectName(u"TextInputFiltro")
        self.TextInputFiltro.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TextInputFiltro.sizePolicy().hasHeightForWidth())
        self.TextInputFiltro.setSizePolicy(sizePolicy2)
        self.TextInputFiltro.setMinimumSize(QSize(200, 0))
        self.TextInputFiltro.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_8.addWidget(self.TextInputFiltro)

        self.ButtonFiltro = QPushButton(self.ToolsFilterNav)
        self.ButtonFiltro.setObjectName(u"ButtonFiltro")
        self.ButtonFiltro.setMinimumSize(QSize(30, 0))
        self.ButtonFiltro.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.ButtonFiltro)


        self.horizontalLayout_6.addWidget(self.ToolsFilterNav)

        self.ToolsButtonsNav = QFrame(self.ToolsFrameTop)
        self.ToolsButtonsNav.setObjectName(u"ToolsButtonsNav")
        sizePolicy2.setHeightForWidth(self.ToolsButtonsNav.sizePolicy().hasHeightForWidth())
        self.ToolsButtonsNav.setSizePolicy(sizePolicy2)
        self.ToolsButtonsNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolsButtonsNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.ToolsButtonsNav)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.ButtonTransferirTools = QPushButton(self.ToolsButtonsNav)
        self.ButtonTransferirTools.setObjectName(u"ButtonTransferirTools")

        self.horizontalLayout_7.addWidget(self.ButtonTransferirTools)

        self.ButtonEditarTools = QPushButton(self.ToolsButtonsNav)
        self.ButtonEditarTools.setObjectName(u"ButtonEditarTools")

        self.horizontalLayout_7.addWidget(self.ButtonEditarTools)

        self.ButtonAdicionarTools = QPushButton(self.ToolsButtonsNav)
        self.ButtonAdicionarTools.setObjectName(u"ButtonAdicionarTools")

        self.horizontalLayout_7.addWidget(self.ButtonAdicionarTools)


        self.horizontalLayout_6.addWidget(self.ToolsButtonsNav, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.ToolsFrameTop)

        self.ToolsTableWidget = QTableWidget(self.ToolsPage)
        if (self.ToolsTableWidget.columnCount() < 7):
            self.ToolsTableWidget.setColumnCount(7)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.ToolsTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        self.ToolsTableWidget.setObjectName(u"ToolsTableWidget")
        self.ToolsTableWidget.setStyleSheet(u"")
        self.ToolsTableWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolsTableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.ToolsTableWidget.setLineWidth(1)
        self.ToolsTableWidget.setMidLineWidth(0)
        self.ToolsTableWidget.setAutoScrollMargin(16)
        self.ToolsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ToolsTableWidget.setTabKeyNavigation(False)
        self.ToolsTableWidget.setProperty(u"showDropIndicator", False)
        self.ToolsTableWidget.setDragEnabled(False)
        self.ToolsTableWidget.setDragDropOverwriteMode(False)
        self.ToolsTableWidget.setAlternatingRowColors(True)
        self.ToolsTableWidget.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.ToolsTableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ToolsTableWidget.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.ToolsTableWidget.setShowGrid(True)
        self.ToolsTableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.ToolsTableWidget.setSortingEnabled(True)
        self.ToolsTableWidget.setWordWrap(True)
        self.ToolsTableWidget.setCornerButtonEnabled(True)
        self.ToolsTableWidget.setRowCount(0)
        self.ToolsTableWidget.setColumnCount(7)
        self.ToolsTableWidget.horizontalHeader().setVisible(True)
        self.ToolsTableWidget.horizontalHeader().setHighlightSections(False)
        self.ToolsTableWidget.verticalHeader().setVisible(True)
        self.ToolsTableWidget.verticalHeader().setHighlightSections(False)
        self.ToolsTableWidget.verticalHeader().setProperty(u"showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.ToolsTableWidget)

        self.BodyWidget.addWidget(self.ToolsPage)
        self.ViewLocalPage = QWidget()
        self.ViewLocalPage.setObjectName(u"ViewLocalPage")
        self.verticalLayout_4 = QVBoxLayout(self.ViewLocalPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ViewLocalFrameTop = QFrame(self.ViewLocalPage)
        self.ViewLocalFrameTop.setObjectName(u"ViewLocalFrameTop")
        self.ViewLocalFrameTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.ViewLocalFrameTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.ViewLocalFrameTop)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.LabelViewLocalLogo = QLabel(self.ViewLocalFrameTop)
        self.LabelViewLocalLogo.setObjectName(u"LabelViewLocalLogo")
        self.LabelViewLocalLogo.setFont(font1)

        self.horizontalLayout_12.addWidget(self.LabelViewLocalLogo, 0, Qt.AlignmentFlag.AlignLeft)

        self.ViewLocalMidFrame = QFrame(self.ViewLocalFrameTop)
        self.ViewLocalMidFrame.setObjectName(u"ViewLocalMidFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.ViewLocalMidFrame.sizePolicy().hasHeightForWidth())
        self.ViewLocalMidFrame.setSizePolicy(sizePolicy3)
        self.ViewLocalMidFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ViewLocalMidFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.ViewLocalMidFrame)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(10, 0, 10, 0)
        self.labelresponsavellogo = QLabel(self.ViewLocalMidFrame)
        self.labelresponsavellogo.setObjectName(u"labelresponsavellogo")
        self.labelresponsavellogo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.labelresponsavellogo, 0, Qt.AlignmentFlag.AlignLeft)

        self.LabelViewLocalResponsavel = QLabel(self.ViewLocalMidFrame)
        self.LabelViewLocalResponsavel.setObjectName(u"LabelViewLocalResponsavel")
        self.LabelViewLocalResponsavel.setScaledContents(False)
        self.LabelViewLocalResponsavel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.LabelViewLocalResponsavel.setWordWrap(False)

        self.horizontalLayout_14.addWidget(self.LabelViewLocalResponsavel, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.ViewLocalMidFrame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_14.addWidget(self.frame_2)


        self.horizontalLayout_12.addWidget(self.ViewLocalMidFrame)

        self.ViewLocalButtonNav = QFrame(self.ViewLocalFrameTop)
        self.ViewLocalButtonNav.setObjectName(u"ViewLocalButtonNav")
        self.ViewLocalButtonNav.setFrameShape(QFrame.Shape.StyledPanel)
        self.ViewLocalButtonNav.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.ViewLocalButtonNav)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ButtonTransferirViewLocal = QPushButton(self.ViewLocalButtonNav)
        self.ButtonTransferirViewLocal.setObjectName(u"ButtonTransferirViewLocal")

        self.horizontalLayout_13.addWidget(self.ButtonTransferirViewLocal)

        self.ButtonEditarViewLocal = QPushButton(self.ViewLocalButtonNav)
        self.ButtonEditarViewLocal.setObjectName(u"ButtonEditarViewLocal")

        self.horizontalLayout_13.addWidget(self.ButtonEditarViewLocal)

        self.ButtonAdicionarViewLocal = QPushButton(self.ViewLocalButtonNav)
        self.ButtonAdicionarViewLocal.setObjectName(u"ButtonAdicionarViewLocal")

        self.horizontalLayout_13.addWidget(self.ButtonAdicionarViewLocal)


        self.horizontalLayout_12.addWidget(self.ViewLocalButtonNav, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_4.addWidget(self.ViewLocalFrameTop)

        self.ViewLocalTableWidget = QTableWidget(self.ViewLocalPage)
        if (self.ViewLocalTableWidget.columnCount() < 6):
            self.ViewLocalTableWidget.setColumnCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.ViewLocalTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.ViewLocalTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.ViewLocalTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.ViewLocalTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.ViewLocalTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.ViewLocalTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.ViewLocalTableWidget.setObjectName(u"ViewLocalTableWidget")

        self.verticalLayout_4.addWidget(self.ViewLocalTableWidget)

        self.BodyWidget.addWidget(self.ViewLocalPage)

        self.verticalLayout.addWidget(self.BodyWidget)

        self.FooterFrame = QFrame(self.centralwidget)
        self.FooterFrame.setObjectName(u"FooterFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.FooterFrame.sizePolicy().hasHeightForWidth())
        self.FooterFrame.setSizePolicy(sizePolicy4)
        self.FooterFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FooterFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FooterFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FooterLeftFrame = QFrame(self.FooterFrame)
        self.FooterLeftFrame.setObjectName(u"FooterLeftFrame")
        self.FooterLeftFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FooterLeftFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.FooterLeftFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LabelVersion = QLabel(self.FooterLeftFrame)
        self.LabelVersion.setObjectName(u"LabelVersion")

        self.horizontalLayout_5.addWidget(self.LabelVersion)


        self.horizontalLayout_3.addWidget(self.FooterLeftFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.FooterRightFrame = QFrame(self.FooterFrame)
        self.FooterRightFrame.setObjectName(u"FooterRightFrame")
        self.FooterRightFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FooterRightFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.FooterRightFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ButtonContato = QPushButton(self.FooterRightFrame)
        self.ButtonContato.setObjectName(u"ButtonContato")

        self.horizontalLayout_4.addWidget(self.ButtonContato)

        self.ButtonSuporte = QPushButton(self.FooterRightFrame)
        self.ButtonSuporte.setObjectName(u"ButtonSuporte")

        self.horizontalLayout_4.addWidget(self.ButtonSuporte)


        self.horizontalLayout_3.addWidget(self.FooterRightFrame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.FooterFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.BodyWidget.setCurrentIndex(0)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Swork", None))
        self.ButtonInicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.ButtonLocais.setText(QCoreApplication.translate("MainWindow", u"Locais", None))
        self.ButtonFerramentas.setText(QCoreApplication.translate("MainWindow", u"Ferramentas", None))
        self.labelLogo.setText(QCoreApplication.translate("MainWindow", u"SWork", None))
        self.LocalsLabelHeader.setText(QCoreApplication.translate("MainWindow", u"Locais", None))
        self.ButtonEditarLocals.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.ButtonAdicionarLocals.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.tools_label_header.setText(QCoreApplication.translate("MainWindow", u"Ferramentas", None))
        self.toolslabelfiltro.setText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.ButtonFiltro.setText("")
        self.ButtonTransferirTools.setText(QCoreApplication.translate("MainWindow", u"Transferir", None))
        self.ButtonEditarTools.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.ButtonAdicionarTools.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.LabelViewLocalLogo.setText(QCoreApplication.translate("MainWindow", u"ViewLocal", None))
        self.labelresponsavellogo.setText(QCoreApplication.translate("MainWindow", u"Respons\u00e1vel :", None))
        self.LabelViewLocalResponsavel.setText(QCoreApplication.translate("MainWindow", u"Nome do responsavel", None))
        self.ButtonTransferirViewLocal.setText(QCoreApplication.translate("MainWindow", u"Transferir", None))
        self.ButtonEditarViewLocal.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.ButtonAdicionarViewLocal.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.LabelVersion.setText(QCoreApplication.translate("MainWindow", u"Open Source | test version 1.0 | in progress...", None))
        self.ButtonContato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.ButtonSuporte.setText(QCoreApplication.translate("MainWindow", u"Suporte", None))
    # retranslateUi

