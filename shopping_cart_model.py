from dataclasses import dataclass
from typing import List

from item import item


@dataclass
class the_cart(object):
    items: List[item]

    def total(self):
        if len(self.items) > 0:
            return self.items[0].unit_price
        return 0
