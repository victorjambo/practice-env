import sqlite3


class DBManager(sqlite3):
    """docstring for DBManager"""
    def __init__(self, arg):
        super(DBManager, self).__init__()
        self.arg = arg

    def migration(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def select(self):
        pass

    def select_one(self):
        pass
