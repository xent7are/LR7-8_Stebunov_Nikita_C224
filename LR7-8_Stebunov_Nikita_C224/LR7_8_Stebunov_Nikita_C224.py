# -*- coding: cp1251 -*-
# ������ ������ pdb (Python Debugger) ��� ������� ����
import pdb

# �������� ������� ������� ��� �������� ��������
questions = {}

mail = 'ADRESS'
text = 'QUEST'

# ���������� � ������� questions ������ � ������ mail � ��������� text
questions[mail] = text

# ��������� ����� �������� ��� ������� � ������� pdb
pdb.set_trace()