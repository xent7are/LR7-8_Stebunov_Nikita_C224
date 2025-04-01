# -*- coding: cp1251 -*-
# Импорт модуля pdb (Python Debugger) для отладки кода
import pdb

# Создание пустого словаря для хранения вопросов
questions = {}

# Установка точки останова для отладки с помощью pdb
pdb.set_trace()

mail = 'ADRESS'
text = 'QUEST'

# Добавление в словарь questions записи с ключом mail и значением text
questions[mail] = text