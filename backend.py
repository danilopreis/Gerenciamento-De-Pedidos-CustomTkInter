import sqlite3


class Banco:

    def connect_db(self):
        self.conn = sqlite3.connect("sistema_gp_fusiontec.db")
        self.cursor = self.conn.cursor()

    def disconnect_db(self):
        self.conn.close()