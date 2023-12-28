from enum import Enum


class ConsoleUiRoutingState(Enum):
    INITIALIZED = 0
    ACCOUNT_REGISTER = 1
    LOGIN = 2
    LOGOUT = 3
    ACCOUNT_DELETE = 4
