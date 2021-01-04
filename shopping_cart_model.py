from dataclasses import dataclass
from functools import reduce
from typing import List
from item import item


@dataclass
class the_cart(object):
    items: List[item]

    def total(self):
        return reduce(lambda subtotal, item: subtotal + (item.unit_price * item.quantity), self.items, 0)
