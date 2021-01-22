from typing import TypedDict  # type: ignore
import os


class ConfigVars(TypedDict):
    """
    Used to define the dict types in a strict way.
    """
    ip_address: str
    database: str
    user: str
    password: str
    warehouse: str
    account: str


def get_variables() -> ConfigVars:
    """
    get_variables is used to access environmental variables
    :return:
    """
    try:
        ip_address = os.environ['IP_ADDRESS']
        database = os.environ['DATABASE']
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        account = os.environ['ACCOUNT']
        warehouse = os.environ['WAREHOUSE']
    except KeyError:
        raise KeyError("Please verify that the needed env variables are set")
    return {"ip_address": ip_address,
            "user": user,
            "database": database,
            "password": password,
            "account": account,
            "warehouse": warehouse}
