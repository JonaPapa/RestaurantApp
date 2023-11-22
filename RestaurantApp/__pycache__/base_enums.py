from enum import Enum
class OrderItemSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XXL = 4
    
class Location(Enum):
    ALBANIA = 1
    KOSOVA = 2

class ApplicationMode(Enum):
    ORDER = 1
    TABLE_RESERVATION = 2
    CANCEL_RESERVATION = 3