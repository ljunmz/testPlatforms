from task.dbUitls import MysqlHelper

mh = MysqlHelper('47.112.0.183', 'planadmin', 'pL%5^an3a$4in', 'automation')


def findStatusById(params):
    sql = "SELECT * FROM automation.task where taskId=%s"
    return mh.find(sql, params)
