from view.display_builder import Display

class Home(Display):
    def __init__(self):
        """
        Initializes the HomeScreen display.
        """
        super().__init__()
        
    def display(self) -> str:
        """
        Displays the home screen menu and gets the user's command.
        
        Returns:
            str: The user's command input.
        """
        message = '''
        Sistema Tri-Calculator

        * Primeira Calculadora - 1
        * Segunda Calculadora - 2
        * Terceira Calculadora - 3
        * Sair - 0
        '''

        self.show_message(message)
        command = input("\nInsira o comando:")
        return command
