from flask import Flask

from main.calculator import CalculatorRoutes

if __name__ == "__main__":
    app = Flask(__name__)

    calculator_controller = CalculatorRoutes(app=app)

    app.run(port=3000)
