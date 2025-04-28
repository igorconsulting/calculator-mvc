from control.calculator import CalculatorController
from flask import Flask

if __name__=="__main__":
    app = Flask(__name__)

    calculator_controller = CalculatorController(app=app)

    app.run(port=3000)

