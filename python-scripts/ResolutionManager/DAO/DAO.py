"""
The database handler for the mysql data
Created by adam on 8/14/17
"""
__author__ = 'adam'

from sqlalchemy import create_engine
from ResolutionManager.config.Configuration import Configuration

class Dao(object):

    def __init__(self):
        self.conn = None
        self.engine = None

    def connect(self, test=False, local=False):
        pass
#
# class SqliteDao:
#
#     def __init__( self ):
#         self.records = [ ]
#         self.SAVED_DATA = ''
#         self.connect()
#
#     def connect( self, test=False, local=True ):
#         """
#         @param test True connects to test database locally (still must specify local as true)
#         @type test string
#         @param local True connects to localhost; False connects to adamnet
#         @type local string
#         """
#         dsn = "sqlite:///{}".format( self.db_location )
#         print( "Connecting to {}".format( dsn ) )
#         self.engine = create_engine( dsn )


class MySqlDao(Dao):
    """
    This handles interactions with mysql databases
    """

    def __init__( self, test=False, local=False ):
        self.records = [ ]
        self.SAVED_DATA = ''
        self.connect( test, local )

    def connect( self, test=False, local=False ):
        """
        @param test True connects to test database locally (still must specify local as true)
        @type test string
        @param local True connects to localhost; False connects to adamnet
        @type local string
        """
        config = Configuration()

        #     """ local db """
        dsn = "mysql+mysqlconnector://root:@127.0.0.1:3306/ascsu"
        self.engine = create_engine( config.dsn )
        self.conn = self.engine.connect()


if __name__ == '__main__':
    pass
