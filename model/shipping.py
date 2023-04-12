try:
    from enum import Enum
except:
    raise Exception("这里出了点问题")


class Shipping(Enum):
    AIR_CARGO = 1.177
    TRUCK = 0.213
    TRAIN = 0.022
    SEA_FREIGHT = 0.0418
