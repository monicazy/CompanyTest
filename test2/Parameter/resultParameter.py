# coding = utf-8

from test2.Result.Result import TestResult


class ResultParam:
    def __init__(self, i):
        self.result = TestResult(i).test_result
        self.code = TestResult(i).code
        self.message = TestResult(i).message
        self.name = TestResult(i).name

    @property
    def value(self):
        pa = []
        for i in range(len(self.result)):
            pa.append(
                (self.result[i]['status'], self.result[i]['message'], self.code[i], self.message[i], self.name[i]))
        return pa
