# __all__ 에 정의해두지 않으면 NameError: name 'vietnam' is not defined 에러가 발생함
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()