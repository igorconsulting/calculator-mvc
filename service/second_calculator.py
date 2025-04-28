from numpy import std
from math import pow

class SecondCalculator:
    def __init__(self, num_list: list[float]):
        self.num_list = num_list

    def part_1(self) -> list[float]:
        final_list = []
        for num in self.num_list:
            result = num*11
            result = pow(result,0.95)
            final_list.append(result)

        return final_list

    def part_2(self,result_list:list[float]) -> float:
        std_value = std(result_list)
        return 1/std_value
    
    def calculate(self) -> float:
        result = self.part_1()
        return self.part_2(result)
