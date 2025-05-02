from main.calculus import CalculusManager

calculus = CalculusManager()


class FirstCalculator:
    def __init__(self, value: float):
        self.value = value

    def calculate(self) -> float:
        v1, v2, v3 = self.__divide(self.value)

        r1 = self.__part_1(v1)
        r2 = self.__part_2(v2)
        r3 = self.__part_3(v3)

        return self.__part_4([r1, r2, r3])

    def __divide(self, value: float) -> list[float]:
        return [value / 3, value / 3, value / 3]

    def __part_1(self, value: float) -> float:
        result = value / 4
        result = result + 7
        result = calculus.sqrt(result)
        result = 0.257 * result

        return result

    def __part_2(self, value: float) -> float:
        result = calculus.pow(value, 2.121)
        result /= 5
        result += 1
        return result

    def __part_3(self, value: float) -> float:
        return value

    def __part_4(self, value_list: list[float]) -> float:
        return calculus.mean(value_list)
