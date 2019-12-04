from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps import app
from apps.model import db

manager = Manager(app)
migrate = Migrate(app, db, render_as_batch=True, compare_type=True)

manager.add_command('db', MigrateCommand)

'''
此文件用来管理数据库的表结构的创建与更新使用

# 初始化 数据库 版本文件 (执行命令后，会在项目跟目录生成migrations文件夹)
python manager.py db init

# 生成 数据库 表结构 文件
python manager.py db migrate

# 映射 表结构 到 数据库中
python manager.py db upgrade

# 多人合作
1. 若有变更直接修改model的Class类
2. 删掉自己的migrations文件夹 与 数据库的 alembic_version表
3. 再执行上面3的命令
'''

if __name__ == '__main__':
    manager.run()
