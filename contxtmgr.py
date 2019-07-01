import sqlite3

# this code is the context manager of the main.py file
# this is responsible for opening and closing the sql database

class DatabaseManager:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None or exc_val is not None or exc_tb is not None:
            self.connection.commit()
        else:
            self.connection.commit()
            self.connection.close()



class MyOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.filename = open(self.filename, self.mode)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_type or exc_val:
            print('Oops! An error occured')
        else:
            self.filename.close()
                


