from PyQt5.QtCore import (QAbstractItemModel, QFile, QIODevice,
    QItemSelectionModel, QModelIndex, Qt)
from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow

import os.path
from settings import SettingsDB


class SPrUTAnaliticsWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SPrUTAnaliticsWindow, self).__init__(parent)

        self.setupUi(self)
        self.settingsdb = SettingsDB()

        self.action_AddAdmin.triggered.connect(self.addAdmin)
        self.pushButtonCreateSDB.clicked.connect(self.createSDB)
        self.isDbExists()

    def isDbExists(self):
        '''
        Функция для проверки наличия базы данных настроек
        и создания ее по команде пользователя, если файл не существует
        '''
        if self.settingsdb.isdbexists:
            # Скрыть кнопку создания файла базы данных настроек
            self.pushButtonCreateSDB.setVisible(False)
            # TODO: Изменить сообщение в информационной строке
            # Проверить наличие Администратора
            # если Администратора нет, то активировать кнопку создания
            # Администратора
            # Если Администратор есть, скрыть кнопку создания
            # Администратора и отобразить сообщение о необходимости входа
            pass
        else:
            # Скрыть кнопку создания Администратора
            self.pushButtonCreateAdmin.setVisible(False)

    def createSDB(self):
        print('Создание SDB')
        pass

    def addAdmin(self):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = SPrUTAnaliticsWindow()
    window.show()
    sys.exit(app.exec_())
