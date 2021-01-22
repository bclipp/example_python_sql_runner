"""
This module is for abstracted interactions with snowflake
"""

import snowflake.connector


class DatabaseManager:
    """
    Used to manage snowflake connection
    """

    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None

    def connect_db(self):
        """
        Used to setup the initial connection to snowflake.
        """
        user = self.config["postgres_user"]
        password = self.config["postgres_password"]
        database = self.config["postgres_db"]
        warehouse = self.config["warehouse"]
        schema = self.config["schema"]
        account = self.config["account"]
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        self.cursor = conn.cursor()
        self.conn = conn
        self.conn.autocommit = True

    def send_sql(self, sql_query: str):
        """
        send_sql is used to send a query but not receive any data.
        :param sql_query:
        """
        try:
            self.cursor.execute(sql_query)
        except snowflake.DatabaseError as error:
            self.conn.rollback()
            # handle better please
            print(error)

    def close_conn(self):
        """
        an abstracted way to control database connection.
        """
        self.cursor.close()
