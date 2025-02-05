from typing import Dict, List, Optional, Union

from .httpclient import HTTPClient
from tcvectordb.model.database import Database


class VectorDBClient():
    """
    VectorDBClient create a http client session for database operate.
    """

    def __init__(self, url=None, username='', key='', timeout=5):
        self._conn = HTTPClient(url, username, key, timeout)

    def create_database(self, database_name: str, timeout: Optional[float] = None) -> Database:
        """Creates a database.

        :param database_name: The name of the database. A database name can only include
        numbers, letters, and underscores, and must not begin with a letter, and length 
        must between 1 and 128
        :type  database_name: str

        :param timeout: An optional duration of time in seconds to allow for the request. When timeout
                        is set to None, will use the connect timeout.
        :type  timeout: float

        :return Database object
        :rtype Database 
        """
        db = Database(self._conn, database_name)
        db.create_database(timeout=timeout)
        return db

    def drop_database(self, database_name: str, timeout: Optional[float] = None):
        """Delete a database.

        :param database_name: The name of the database to delete.
        :type  database_name: str

        :param timeout: An optional duration of time in seconds to allow for the request. When timeout
                        is set to None, will use the connect timeout.
        :type  timeout: float
        """
        db = Database(self._conn, database_name)
        db.drop_database(timeout=timeout)

    def list_databases(self, timeout: Optional[float] = None) -> List[Database]:
        """Get database list.

        :param timeout: An optional duration of time in seconds to allow for the request. When timeout
                        is set to None, will use the connect timeout.
        :type  timeout: float

        :return: The database name list
        :rtype: list[str]
        """
        db = Database(self._conn)
        return db.list_databases(timeout=timeout)

    def database(self, database: str) -> Database:
        """Get database list.

        :param database_name: The name of the database to delete.
        :type  database_name: str

        :return Database object
        :rtype Database 
        """
        db = Database(self._conn, database)
        return db

    def close(self):
        """Close the connect session.

        :param database_name: The name of the database to delete.
        :type  database_name: str

        :return Database object
        :rtype Database 
        """
        if self._conn:
            self._conn.close()
            self._conn = None
