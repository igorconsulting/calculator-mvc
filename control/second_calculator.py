from main.calculus import CalculusManager

calculus = CalculusManager()

class SecondCalculator:
    def __init__(self, num_list: list[float]):
        self.num_list = num_list

    def calculate(self) -> float:
        result = self.__part_1()
        return self.__part_2(result)

    def __part_1(self) -> list[float]:
        final_list = []
        for num in self.num_list:
            result = num*11
            result = calculus.pow(result,0.95)
            final_list.append(result)

        return final_list

    def __part_2(self,result_list:list[float]) -> float:
        std_value = calculus.std(result_list)
        return 1/std_value
    