#factory
from abc import ABC,abstractmethod


class db_factory:
    def get_db_connection(self,db):
        return db.connection(self)


#提供一个规范 interface

class data_base(ABC):
    @abstractmethod
    def connection(self):
        pass

class mysql_server:
    def connection(self):
        return ("mysql db connction")


class Oracle_server:
    def connection(self):
        return ("Oracle db connction")



facotry = db_factory()
mysql_conn = facotry.get_db_connection(mysql_server)
oracle_conn = facotry.get_db_connection(Oracle_server)
print(mysql_conn)
print(oracle_conn)