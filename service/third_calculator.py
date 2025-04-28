from numpy import std, var

class ThirdCalculator:
    def __init__(self, num_list: list[float]):
        self.num_list = num_list

    def get_variance(self) -> float:
        return var(self.num_list)

    def get_std(self) -> float:
        return std(self.num_list)
    
    def compare(self) -> bool:
        std_value = self.get_std()
        var_value = self.get_variance()

        return var_value > std_value
