# coding= utf-8

import xlrd


class ReadExcel:
    def __init__(self, path):
        self.path = path

    @property  # 把方法变成属性可以直接进行调用,只有@property表示只读
    def get_sheet(self):
        # 获取索引
        xl = xlrd.open_workbook(self.path)
        sheet = xl.sheets()
        return sheet

    @property
    def get_rows(self):
        # 获取行数
        row = self.sheet.nrows
        return row

    @get_rows.setter         # 有@property and @x.setter表示可读可写;同时有@property和@x.setter和@x.deleter表示可读可写可删除。
    def get_rows(self, sheet):
        self.sheet = sheet

    @property
    def get_col(self):
        # 获取列数
        col = self.sheet.ncols
        return col

    @get_col.setter
    def get_col(self, sheet):
        self.sheet = sheet

    # 以下是分别获取每一列的数值
    @property
    def get_name(self):
        text_name = []
        for i in range(1, self.get_rows):
            text_name.append(self.sheet.cell_value(i, 0))  # append() 方法向列表的尾部添加一个新的元素。只接受一个参数。
        return text_name

    @get_name.setter
    def get_name(self, sheet):
        self.sheet = sheet

    @property
    def get_url(self):
        text_url = []
        for i in range(1, self.get_rows):
            text_url.append(self.sheet.cell_value(i, 1))
        return text_url

    @get_url.setter
    def get_url(self, sheet):
        self.sheet = sheet

    @property
    def get_data(self):
        text_data = []
        for i in range(1, self.get_rows):
            text_data.append(self.sheet.cell_value(i, 2))
        return text_data

    @get_data.setter
    def get_data(self, sheet):
        self.sheet = sheet

    @property
    def get_file(self):
        text_file = []
        for i in range(1, self.get_rows):
            text_file.append(self.sheet.cell_value(i, 3))
        return text_file

    @get_file.setter
    def get_file(self, sheet):
        self.sheet = sheet

    @property
    def get_method(self):
        text_method = []
        for i in range(1, self.get_rows):
            text_method.append(self.sheet.cell_value(i, 4))
        return text_method

    @get_method.setter
    def get_method(self, sheet):
        self.sheet = sheet

    @property
    def get_code(self):
        text_code = []
        for i in range(1, self.get_rows):
            text_code.append(self.sheet.cell_value(i, 5))
        return text_code

    @get_code.setter
    def get_code(self, sheet):
        self.sheet = sheet

    @property
    def get_message(self):
        text_message = []
        for i in range(1, self.get_rows):
            text_message.append(self.sheet.cell_value(i, 6))
        return text_message

    @get_message.setter
    def get_message(self, sheet):
        self.sheet = sheet

    @property
    def get_token(self):
        text_token = []
        for i in range(1, self.get_rows):
            text_token.append(self.sheet.cell_value(i, 7))
        return text_token

    @get_token.setter
    def get_token(self, sheet):
        self.sheet = sheet
