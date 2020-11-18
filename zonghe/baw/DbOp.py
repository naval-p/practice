'''
database op:
1.
'''
from zonghe.caw.MySqlOp import execute, connect, disconnect


def deleteUser(db,phone):
    '''

    :param db: 一个字典，存储数据库信息
    :param phone: 用户注册时的手机号
    :return:
    '''
    conn = connect(db)
    execute(conn,f'delete from Member where mobilephone={phone};')
    disconnect(conn)