# -*- coding: utf-8 -*-

import logging
import os.path
from sqlalchemy import create_engine

# Конфигурируем логинг
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG, filename=u'logs/sa_log.log')


class SettingsDB:
    def isdbexists(self):
        # Проверка существования файла базы данных настроек settings.sq3
        if os.path.isfile('settings.sq3'):
            # TODO: Проверка структуры файла базы настроек
            pass
            # Проверка наличия пользователя Администратор
            return 1
        else:
            # Вернуть значение 0 для подтверждения создания файла базы данных
            return 0

            # TODO: Создание таблицы пользователей приложения
# engine = create_engine('sqlite:///settings.sq3')

if __name__ == '__main__':
    settingsdb = SettingsDB()

    isdbexist = settingsdb.isdbexists()
    print(isdbexist)
