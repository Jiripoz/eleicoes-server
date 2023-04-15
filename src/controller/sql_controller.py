from src.controller.query_commands.insert import Insert
from src.controller.query_commands.delete import Delete
from src.controller.query_commands.select import Select


class SQLController:
    def __init__(self, conn, cur):
        self.insert = Insert(cur)
        self.delete = Delete(cur)
        self.select = Select(cur)
        self.conn = conn   
