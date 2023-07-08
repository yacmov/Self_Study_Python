import Theater_module
Theater_module.price(1) # 1 person normal price
Theater_module.price_morning(0) # none going to 
Theater_module.price_soldier(4) # 4 soldier go to

import Theater_module as mv
mv.price(1)
mv.price_morning(0)
mv.price_soldier(4)

from Theater_module import *
price(1)
price_morning(0)
price_soldier(4)

from Theater_module import (price, price_morning)
price(5)
price_morning(3)
price_soldier(1)


from Theater_module import price_soldier as price
price(4)