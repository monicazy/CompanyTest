# coding = utf-8

import os
from ReadExcel.readExcel import ReadExcel
import Case

default_excel_filename = 'test_case.xls'  # TODO: make this configurable
default_excel = ReadExcel(os.path.join(os.path.dirname(Case.__file__), default_excel_filename))