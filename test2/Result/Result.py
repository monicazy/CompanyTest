# coding = utf-8

from test2.ReadExcel import default_excel
from test2.Method.TestMethod import TestApi
from test2.Cookie.Cookies import cookie

excel = default_excel


class TestResult:
    def __init__(self, i):
        self.sheet = excel.get_sheet[i]
        excel.get_name = self.sheet
        self.name = excel.get_name
        excel.get_url = self.sheet
        self.url = excel.get_url
        excel.get_data = self.sheet
        self.data = excel.get_data
        excel.get_method = self.sheet
        self.method = excel.get_method
        excel.get_code = self.sheet
        self.code = excel.get_code
        excel.get_message = self.sheet
        self.message = excel.get_message
        excel.get_token = self.sheet
        self.token = excel.get_token
        # 获取行数
        excel.get_rows = self.sheet
        self.row = excel.get_rows
        excel.get_file = self.sheet
        self.file = excel.get_file

    @property
    def test_result(self):
        text_result = []
        for i in range(0, self.row - 1):
            try:
                if self.token[i] == 0:
                    api = TestApi(self.method[i], self.url[i], self.data[i]).test_api
                    if api.status_code == 200:
                        text_result.append(api.json())
                    else:
                        text_result.append({"status": api.status_code, "message": "HTTP状态码错误，接口请求失败"})
                elif self.token[i] == 1:
                    api = TestApi(self.method[i], self.url[i], self.data[i], None, cookie).test_api
                    if api.status_code == 200:
                        text_result.append(api.json())
                    else:
                        text_result.append({"status": api.status_code, "message": "HTTP状态码错误，接口请求失败"})
                else:
                    api = TestApi(self.method[i], self.url[i], self.data[i], {'upload_file': open(self.file[i], 'rb')},cookie).test_api
                    if api.status_code == 200:
                        text_result.append(api.json())
                    else:
                        text_result.append({"status": api.status_code, "message": "HTTP状态码错误，接口请求失败"})
            except Exception as e:
                text_result.append({"status": -1, "message": str(e)+":未知错误(接口请求超时或传递数据错误等)"})
        return text_result
