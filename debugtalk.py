from pymysql.cursors import DictCursor

from common import mysql_handler, excel_hander, yaml_hander
import time


def sleep(n_secs):
    time.sleep(n_secs)


def get_phone():
    import random
    phone = "1" + random.choice(["3", "5"])
    for i in range(9):
        num = random.randint(0, 9)
        phone = phone + str(num)
    return phone


def read_excel_data():
    data_path = r"F:\python\python_hrun\data\testdata.xlsx"
    data = excel_hander.ExcelHandler(data_path).read_sheet_data("register")
    return data[0]["mobile_phone"]


def get_sql_data():
    SQL = mysql_handler.MySQLHandler(
        host="120.78.128.25",
        port=3306,
        user="future",
        password="123456",
        charset="utf8",
        cursorclass=DictCursor
    )
    phone = read_excel_data()
    phone_sql = "select * from futureloan.member where  mobile_phone={};".format(phone)
    phone_recode = SQL.select_data(phone_sql)
    if phone_recode:
        return phone_recode["mobile_phone"]


if __name__ == '__main__':
    print(get_sql_data())
