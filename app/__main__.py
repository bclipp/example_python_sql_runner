"""
    This app is used for importing data
"""

import modules.sql as sql
import modules.utils as utils
import modules.database as database


def main():
    """
    THe main entry point for the running SQL to load exported data into snowflake
    """

    config: utils.ConfigVars = utils.get_variables()
    query: str = sql.load_data("my_table", "s3://..")
    database_manager: database.DatabaseManager = database.DatabaseManager(config)
    database_manager.connect(config)
    database_manager.send_query(query)


if __name__ == "__main__":
    main()
