DEBUG = True
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '192.168.52.53'
PORT = 3306
DATABASE = 'flask'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                          PORT, DATABASE)
