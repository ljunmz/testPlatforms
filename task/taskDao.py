from task.dbUitls import MysqlHelper

mh = MysqlHelper('192.168.16.8', 'planadmin', 'pL%5^an3a$4in', 'automation')


def findStatusById(params):
    sql = "SELECT * FROM automation.task where taskId=%s"
    return mh.find(sql, params)
