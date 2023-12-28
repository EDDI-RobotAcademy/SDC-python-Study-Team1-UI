from enum import Enum


class CustomProtocol(Enum):
    ACCOUNT_REGISTER = 1
    ACCOUNT_LOGIN = 2
    ACCOUNT_REMOVE = 3
    ACCOUNT_LOGOUT = 4
    # PRODUCT_LIST = 4
    # PRODUCT_REGISTER = 5
    # PRODUCT_READ = 6
    # PRODUCT_PURCHASE = 7
    # PRODUCT_REMOVE = 8
    # ORDER_LIST = 9
    EXIT = 10
