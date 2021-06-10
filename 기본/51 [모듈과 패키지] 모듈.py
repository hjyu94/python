import theater_module # 1
import theater_module as mv # 2
from theater_module import * # 3
from theater_module import price, price_morning
from theater_module import price_morning as pm # 4

# 1
theater_module.price(3)
theater_module.price_morning(4)

# 2
mv.price(3)
mv.price_morning(4)

# 3
price(3)
price_morning(4)

# 4
pm(4)