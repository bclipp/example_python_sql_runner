"""
This module is for storing general SQL statements
"""


def load_data(table: str, location: str) -> str:
    """
    SQL statement to load data from S3
    :param table: table to load data into,ex: customers
    :param location: locaiton of the file,ex: s3://mybucket/unload/
    """
    # return f"""DROP TABLE {table}; """
    return f"""
    COPY INTO {location}
    FROM {table}
    storage_integration = aws_int
    file_format = (format_name = json_format); """
