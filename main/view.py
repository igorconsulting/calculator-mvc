from control.calculator import CalculatorController
from view.display_builder import Display
from view.home import Home


class ViewController(Display):
    def __init__(self):
        super().__init__()
        self.home = Home()
        self.calculator = CalculatorController()
        self.routes = {
            "1": lambda: self.calculator.run("1"),
            "2": lambda: self.calculator.run("2"),
            "3": lambda: self.calculator.run("3"),
            "0": self.exit_app,
        }

    def move_screen(self, command: str) -> None:
        """
        Routes the user command to the appropriate controller action using a dispatch table.
        """
        action = self.routes.get(command, self.invalid_command)
        action()

    def exit_app(self):
        self.show_message("Saindo do sistema. Obrigado!")
        exit()

    def invalid_command(self):
        self.show_message("Comando inválido. Tente novamente.")

    def display(self) -> None:
        """
        Main loop: displays the menu and routes the user input.
        """
        while True:
            command = self.home.display()
            self.move_screen(command)
