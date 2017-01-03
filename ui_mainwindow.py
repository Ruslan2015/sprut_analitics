# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 696)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.InfoLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InfoLabel.sizePolicy().hasHeightForWidth())
        self.InfoLabel.setSizePolicy(sizePolicy)
        self.InfoLabel.setMinimumSize(QtCore.QSize(0, 15))
        self.InfoLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.InfoLabel.setFont(font)
        self.InfoLabel.setObjectName("InfoLabel")
        self.horizontalLayout.addWidget(self.InfoLabel)
        self.pushButtonCreateSDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCreateSDB.setFlat(False)
        self.pushButtonCreateSDB.setObjectName("pushButtonCreateSDB")
        self.horizontalLayout.addWidget(self.pushButtonCreateSDB)
        self.pushButtonCreateAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCreateAdmin.setObjectName("pushButtonCreateAdmin")
        self.horizontalLayout.addWidget(self.pushButtonCreateAdmin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabMainWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabMainWidget.setObjectName("tabMainWidget")
        self.tab1MW = QtWidgets.QWidget()
        self.tab1MW.setObjectName("tab1MW")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab1MW)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.treeView = QtWidgets.QTreeView(self.tab1MW)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout_3.addWidget(self.treeView)
        self.verticalLayoutMainTab = QtWidgets.QVBoxLayout()
        self.verticalLayoutMainTab.setObjectName("verticalLayoutMainTab")
        self.textEditListFullText = QtWidgets.QTextEdit(self.tab1MW)
        self.textEditListFullText.setObjectName("textEditListFullText")
        self.verticalLayoutMainTab.addWidget(self.textEditListFullText)
        self.tabVLMTWidget = QtWidgets.QTabWidget(self.tab1MW)
        self.tabVLMTWidget.setObjectName("tabVLMTWidget")
        self.tab1VLMT = QtWidgets.QWidget()
        self.tab1VLMT.setObjectName("tab1VLMT")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab1VLMT)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelNumOfExe = QtWidgets.QLabel(self.tab1VLMT)
        self.labelNumOfExe.setObjectName("labelNumOfExe")
        self.verticalLayout_4.addWidget(self.labelNumOfExe)
        self.scrollArea = QtWidgets.QScrollArea(self.tab1VLMT)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContentsCheckExe = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsCheckExe.setGeometry(QtCore.QRect(0, 0, 449, 133))
        self.scrollAreaWidgetContentsCheckExe.setObjectName("scrollAreaWidgetContentsCheckExe")
        self.scrollArea.setWidget(self.scrollAreaWidgetContentsCheckExe)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.tabVLMTWidget.addTab(self.tab1VLMT, "")
        self.tab2VLMT = QtWidgets.QWidget()
        self.tab2VLMT.setObjectName("tab2VLMT")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab2VLMT)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEditInfoReg = QtWidgets.QTextEdit(self.tab2VLMT)
        self.textEditInfoReg.setObjectName("textEditInfoReg")
        self.verticalLayout_3.addWidget(self.textEditInfoReg)
        self.tabVLMTWidget.addTab(self.tab2VLMT, "")
        self.verticalLayoutMainTab.addWidget(self.tabVLMTWidget)
        self.horizontalLayoutVLMT = QtWidgets.QHBoxLayout()
        self.horizontalLayoutVLMT.setObjectName("horizontalLayoutVLMT")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab1MW)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayoutVLMT.addWidget(self.textBrowser)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab1MW)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayoutVLMT.addWidget(self.calendarWidget)
        self.verticalLayoutMainTab.addLayout(self.horizontalLayoutVLMT)
        self.horizontalLayout_3.addLayout(self.verticalLayoutMainTab)
        self.tabMainWidget.addTab(self.tab1MW, "")
        self.tab2MW = QtWidgets.QWidget()
        self.tab2MW.setObjectName("tab2MW")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab2MW)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowserSPrUT = QtWidgets.QTextBrowser(self.tab2MW)
        self.textBrowserSPrUT.setObjectName("textBrowserSPrUT")
        self.verticalLayout_2.addWidget(self.textBrowserSPrUT)
        self.tabMainWidget.addTab(self.tab2MW, "")
        self.verticalLayout.addWidget(self.tabMainWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_DB = QtWidgets.QMenu(self.menubar)
        self.menu_DB.setObjectName("menu_DB")
        self.menu_Connections = QtWidgets.QMenu(self.menu_DB)
        self.menu_Connections.setEnabled(False)
        self.menu_Connections.setObjectName("menu_Connections")
        self.menuSQLite = QtWidgets.QMenu(self.menu_Connections)
        self.menuSQLite.setObjectName("menuSQLite")
        self.menu_Connect = QtWidgets.QMenu(self.menu_DB)
        self.menu_Connect.setEnabled(False)
        self.menu_Connect.setObjectName("menu_Connect")
        self.menu_Tree = QtWidgets.QMenu(self.menubar)
        self.menu_Tree.setObjectName("menu_Tree")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_Admin = QtWidgets.QMenu(self.menu)
        self.menu_Admin.setEnabled(False)
        self.menu_Admin.setObjectName("menu_Admin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_ImportFromExcel = QtWidgets.QAction(MainWindow)
        self.action_ImportFromExcel.setEnabled(False)
        self.action_ImportFromExcel.setObjectName("action_ImportFromExcel")
        self.action_ExportToExcel = QtWidgets.QAction(MainWindow)
        self.action_ExportToExcel.setEnabled(False)
        self.action_ExportToExcel.setObjectName("action_ExportToExcel")
        self.action_Print = QtWidgets.QAction(MainWindow)
        self.action_Print.setEnabled(False)
        self.action_Print.setObjectName("action_Print")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_BackUp = QtWidgets.QAction(MainWindow)
        self.action_BackUp.setEnabled(False)
        self.action_BackUp.setObjectName("action_BackUp")
        self.action_Restore = QtWidgets.QAction(MainWindow)
        self.action_Restore.setEnabled(False)
        self.action_Restore.setObjectName("action_Restore")
        self.action_AddRoot = QtWidgets.QAction(MainWindow)
        self.action_AddRoot.setEnabled(False)
        self.action_AddRoot.setObjectName("action_AddRoot")
        self.action_AddBranche = QtWidgets.QAction(MainWindow)
        self.action_AddBranche.setEnabled(False)
        self.action_AddBranche.setObjectName("action_AddBranche")
        self.action_DelBranche = QtWidgets.QAction(MainWindow)
        self.action_DelBranche.setEnabled(False)
        self.action_DelBranche.setObjectName("action_DelBranche")
        self.action_DelRoot = QtWidgets.QAction(MainWindow)
        self.action_DelRoot.setEnabled(False)
        self.action_DelRoot.setObjectName("action_DelRoot")
        self.action_AddItem = QtWidgets.QAction(MainWindow)
        self.action_AddItem.setEnabled(False)
        self.action_AddItem.setObjectName("action_AddItem")
        self.action_DelItem = QtWidgets.QAction(MainWindow)
        self.action_DelItem.setEnabled(False)
        self.action_DelItem.setObjectName("action_DelItem")
        self.action_NetworkRegistration = QtWidgets.QAction(MainWindow)
        self.action_NetworkRegistration.setEnabled(False)
        self.action_NetworkRegistration.setObjectName("action_NetworkRegistration")
        self.action_NetworkLogin = QtWidgets.QAction(MainWindow)
        self.action_NetworkLogin.setEnabled(False)
        self.action_NetworkLogin.setObjectName("action_NetworkLogin")
        self.action_LocalRegistration = QtWidgets.QAction(MainWindow)
        self.action_LocalRegistration.setEnabled(False)
        self.action_LocalRegistration.setObjectName("action_LocalRegistration")
        self.action_LocalLogin = QtWidgets.QAction(MainWindow)
        self.action_LocalLogin.setEnabled(False)
        self.action_LocalLogin.setObjectName("action_LocalLogin")
        self.action_NewSQLiteFile = QtWidgets.QAction(MainWindow)
        self.action_NewSQLiteFile.setObjectName("action_NewSQLiteFile")
        self.action_SelectSQLiteFile = QtWidgets.QAction(MainWindow)
        self.action_SelectSQLiteFile.setObjectName("action_SelectSQLiteFile")
        self.action_ConnectSelSQLite = QtWidgets.QAction(MainWindow)
        self.action_ConnectSelSQLite.setObjectName("action_ConnectSelSQLite")
        self.action_AddAdmin = QtWidgets.QAction(MainWindow)
        self.action_AddAdmin.setEnabled(False)
        self.action_AddAdmin.setObjectName("action_AddAdmin")
        self.action_AdminMode = QtWidgets.QAction(MainWindow)
        self.action_AdminMode.setEnabled(False)
        self.action_AdminMode.setObjectName("action_AdminMode")
        self.menu_File.addAction(self.action_ImportFromExcel)
        self.menu_File.addAction(self.action_ExportToExcel)
        self.menu_File.addAction(self.action_Print)
        self.menu_File.addAction(self.action_Exit)
        self.menuSQLite.addAction(self.action_NewSQLiteFile)
        self.menuSQLite.addAction(self.action_SelectSQLiteFile)
        self.menu_Connections.addAction(self.menuSQLite.menuAction())
        self.menu_Connect.addAction(self.action_ConnectSelSQLite)
        self.menu_DB.addAction(self.menu_Connections.menuAction())
        self.menu_DB.addAction(self.menu_Connect.menuAction())
        self.menu_DB.addAction(self.action_BackUp)
        self.menu_DB.addAction(self.action_Restore)
        self.menu_Tree.addAction(self.action_AddRoot)
        self.menu_Tree.addAction(self.action_DelRoot)
        self.menu_Tree.addAction(self.action_AddBranche)
        self.menu_Tree.addAction(self.action_DelBranche)
        self.menu_Tree.addAction(self.action_AddItem)
        self.menu_Tree.addAction(self.action_DelItem)
        self.menu_Admin.addAction(self.action_AddAdmin)
        self.menu_Admin.addAction(self.action_AdminMode)
        self.menu.addAction(self.menu_Admin.menuAction())
        self.menu.addAction(self.action_NetworkRegistration)
        self.menu.addAction(self.action_NetworkLogin)
        self.menu.addAction(self.action_LocalRegistration)
        self.menu.addAction(self.action_LocalLogin)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_DB.menuAction())
        self.menubar.addAction(self.menu_Tree.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabMainWidget.setCurrentIndex(0)
        self.tabVLMTWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.InfoLabel.setText(_translate("MainWindow", "База настроек не создана!"))
        self.pushButtonCreateSDB.setText(_translate("MainWindow", "Создать базу настроек"))
        self.pushButtonCreateAdmin.setText(_translate("MainWindow", "Создать Администратора"))
        self.labelNumOfExe.setText(_translate("MainWindow", "TextLabel"))
        self.tabVLMTWidget.setTabText(self.tabVLMTWidget.indexOf(self.tab1VLMT), _translate("MainWindow", "Регистратор"))
        self.tabVLMTWidget.setTabText(self.tabVLMTWidget.indexOf(self.tab2VLMT), _translate("MainWindow", "Информация"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.tab1MW), _translate("MainWindow", "Аналитика"))
        self.tabMainWidget.setTabText(self.tabMainWidget.indexOf(self.tab2MW), _translate("MainWindow", "СПрУТ"))
        self.menu_File.setTitle(_translate("MainWindow", "Файл"))
        self.menu_DB.setTitle(_translate("MainWindow", "База данных"))
        self.menu_Connections.setTitle(_translate("MainWindow", "Соединения"))
        self.menuSQLite.setTitle(_translate("MainWindow", "SQLite"))
        self.menu_Connect.setTitle(_translate("MainWindow", "Соединиться"))
        self.menu_Tree.setTitle(_translate("MainWindow", "Дерево"))
        self.menu_Help.setTitle(_translate("MainWindow", "Помощь"))
        self.menu.setTitle(_translate("MainWindow", "Пользователи"))
        self.menu_Admin.setTitle(_translate("MainWindow", "Администратор"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_ImportFromExcel.setText(_translate("MainWindow", "Импорт из Excel"))
        self.action_ExportToExcel.setText(_translate("MainWindow", "Экспорт в Excel"))
        self.action_Print.setText(_translate("MainWindow", "Печать"))
        self.action_Exit.setText(_translate("MainWindow", "Выход"))
        self.action_BackUp.setText(_translate("MainWindow", "Резервная копия"))
        self.action_Restore.setText(_translate("MainWindow", "Восстановление"))
        self.action_AddRoot.setText(_translate("MainWindow", "Добавить корень"))
        self.action_AddBranche.setText(_translate("MainWindow", "Добавить ветку"))
        self.action_DelBranche.setText(_translate("MainWindow", "Удалить ветку"))
        self.action_DelRoot.setText(_translate("MainWindow", "Удалить корень"))
        self.action_AddItem.setText(_translate("MainWindow", "Добавить запись"))
        self.action_DelItem.setText(_translate("MainWindow", "Удалить запись"))
        self.action_NetworkRegistration.setText(_translate("MainWindow", "Сетевая регистрация"))
        self.action_NetworkLogin.setText(_translate("MainWindow", "Сетевой вход"))
        self.action_LocalRegistration.setText(_translate("MainWindow", "Локальная регистрация"))
        self.action_LocalLogin.setText(_translate("MainWindow", "Локальный вход"))
        self.action_NewSQLiteFile.setText(_translate("MainWindow", "Создать файл"))
        self.action_SelectSQLiteFile.setText(_translate("MainWindow", "Выбрать файл"))
        self.action_ConnectSelSQLite.setText(_translate("MainWindow", "С выбранным файлом SQLite"))
        self.action_AddAdmin.setText(_translate("MainWindow", "Создать администратора"))
        self.action_AdminMode.setText(_translate("MainWindow", "Режим \"Администратор\""))

