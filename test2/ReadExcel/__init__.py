# coding = utf-8

import os
from test2.ReadExcel.readExcel import ReadExcel
from test2 import Case

default_excel_filename = 'test_case.xlsx'  # TODO: make this configurable
default_excel = ReadExcel(os.path.join(os.path.dirname(Case.__file__), default_excel_filename))