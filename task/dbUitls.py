import pymysql as ps


# ("47.112.0.183", "planadmin", "pL%5^an3a$4in", "thirdparty", charset='utf8')

class MysqlHelper:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = "utf8"
        self.db = None
        self.curs = None

    # 数据库连接
    def open(self):
        self.db = ps.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                             charset=self.charset)
        self.curs = self.db.cursor()

    # 数据库关闭
    def close(self):
        self.curs.close()
        self.db.close()

    # 数据增删改
    def cud(self, sql, params):
        self.open()
        try:
            self.curs.execute(sql, params)
            self.db.commit()
        except:
            print('cud出现错误')
            self.db.rollback()
        self.close()

    # 数据查询
    def find(self, sql, params):
        self.open()
        try:
            self.curs.execute(sql, params)
            self.close()
            return self.curs.fetchall()
        except:
            print('find出现错误')
#
# #
# mh = MysqlHelper('47.112.0.183', 'planadmin', 'pL%5^an3a$4in', 'thirdparty')
# sql = "SELECT * FROM verification_code where device_model=%s"
# re = mh.find(sql, "Meizu-16th Plus")
# print(re)
