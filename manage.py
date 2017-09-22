#! /usr/bin/env python
# -*- coding:utf-8 -*-

__author = 'zealot'

import os
from app import create_app, db
from app.models import User, Role
#from flask.ext.script import Manager, Shell,Server
from flask_script import Manager, Shell,Server
#from flask.ext.migrate import Migrate, MigrateCommand
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("runserver",
                    Server(host="127.0.0.1",
                           port=5000,
                           use_debugger=True))

if __name__ == '__main__':
    manager.run()