from flask import Flask

from control.calculator import CalculatorController

if __name__ == "__main__":
    app = Flask(__name__)

    calculator_controller = CalculatorController(app=app)

    app.run(port=3000)
