import numpy as np
import math

class CalculusManager:
    def __init__(self):
        self.__np = np
        self.__math = math

    def mean(self, value_list: list[float], axis = None) -> float:
        return self.__np.mean(value_list, axis)
    
    def pow(self,value: float, power: float) -> float:
        return self.__math.pow(value,power)
    
    def std(self, value_list: list[float]) -> float:
        return self.__np.std(value_list)
    
    def var(self,value_list: list[float]) -> float:
        return self.__np.var(value_list)
    
    def sqrt(self, value: float) -> float:
        return self.__math.sqrt(value)
    