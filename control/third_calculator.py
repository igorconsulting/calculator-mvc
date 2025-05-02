from main.calculus import CalculusManager

calculator = CalculusManager()


class ThirdCalculator:
    def __init__(self, num_list: list[float]):
        self.num_list = num_list

    def __get_variance(self) -> float:
        return calculator.var(self.num_list)

    def __get_std(self) -> float:
        return calculator.std(self.num_list)

    def compare(self) -> bool:
        std_value = self.__get_std()
        var_value = self.__get_variance()

        return var_value > std_value
