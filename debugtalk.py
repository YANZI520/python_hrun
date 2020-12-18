from pymysql.cursors import DictCursor

from common import mysql_handler, excel_hander
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
    return data


def get_sql_data():
    SQL = mysql_handler.MySQLHandler(
        host="120.78.128.25",
        port=3306,
        user="future",
        password="123456",
        charset="utf8",
        cursorclass=DictCursor
    )
    phone_sql = "select mobile_phone from futureloan.member where  mobile_phone={};".format(read_excel_data()[0]["mobile_phone"])
    phone_recode = SQL.select_data(sql=phone_sql)
    if phone_recode:
        return phone_recode


if __name__ == '__main__':
    print(get_sql_data())
