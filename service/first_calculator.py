import math
from statistics import mean

class FirstCalculator:
    def __init__(self,value: float):
        self.value = value

    def divide(self,value: float)-> list[float]:
        return [value/3,value/3,value/3]
    
    def part_1(self,value: float) -> float:
        result = value/4
        result = result+7
        result = math.sqrt(result)
        result = 0.257*result

        return result
    
    def part_2(self,value: float) -> float:
        result = math.pow(value,2.121)
        result/=5
        result+=1
        return result
    
    def part_3(self,value: float) -> float:
        return value
    
    def part_4(self,value_list:list[float]) -> float:
        return mean(value_list)
    
    def calculate(self) -> float:
        v1,v2,v3 = self.divide(self.value)

        r1 = self.part_1(v1)
        r2 = self.part_2(v2)
        r3 = self.part_3(v3)

        return self.part_4([r1,r2,r3])
