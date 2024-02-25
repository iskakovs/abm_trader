from typing import List, Tuple
import json

class Settings:
    def __init__(self, number_of_days: int,
                 supply_amounts_bounds: Tuple[int, int],
                 supply_volume: List[float], supply_price: List[float],
                 supply_iters: List[int],
                 consumers_amount: int, income_bounds: Tuple[float, float],
                 income_delta: float):
        self.supply_amounts_min, self.supply_amounts_max = supply_amounts_bounds
        if len(supply_volume) > 0:
            self.supply_volume = supply_volume
        else:
            raise ValueError('Supply volume must be positive')
        self.supply_price = supply_price
        self.supply_iters = supply_iters
        self.consumers_amount = consumers_amount
        self.income_min, self.income_max = income_bounds
        self.income_delta = income_delta
        self.number_of_days = number_of_days
