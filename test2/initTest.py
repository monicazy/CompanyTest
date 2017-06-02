# coding = utf-8

import sys
sys.path.append("F:/PythonTest")
import pytest
import logging
from test2.Parameter.resultParameter import ResultParam
from test2.ReadExcel import default_excel
import allure
import _pytest.python
_pytest.python._escape_strings = lambda x: x

logging.basicConfig(level=logging.INFO)

sheets = default_excel.get_sheet


def execute_cases():
    def create_fn(idx, sheet):
        @allure.feature(sheet.name)  # @allure.feature('（Feature1特征）')
        @pytest.mark.parametrize('act_code, act_msg, exp_code, exp_msg, case_name', ResultParam(idx).value)
        def test_fn(act_code, act_msg, exp_code, exp_msg, case_name):
            assert act_code == exp_code
            assert act_msg == exp_msg
            logging.info(case_name)

        return test_fn

    for i, s in enumerate(sheets):
        globals()['test_case_{}'.format(s.name)] = create_fn(i, s)


execute_cases()
