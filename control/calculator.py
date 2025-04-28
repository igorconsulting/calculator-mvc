from flask import Flask, jsonify, request
from service.first_calculator import FirstCalculator
from service.second_calculator import SecondCalculator
from service.third_calculator import ThirdCalculator

class CalculatorController:
    """
    Defines routes to connect with an instance of calculator service
    """
    def __init__(self, app: Flask):
        self.app = app
        self.register_routes()


    def register_routes(self):
        @self.app.route('/first', methods=["POST"])
        def first_calculator():
            body = request.get_json()
            
            try:
                value = self._validate_value(body)
            except (ValueError, TypeError) as e:
                return jsonify({"status": "error", "message": str(e)}), 400

            calculator = FirstCalculator(value)
            result = calculator.calculate()

            return jsonify({"status": "success",
                        "result": result})


        @self.app.route('/second', methods=["POST"])
        def second_calculator():
            body = request.get_json()
            try:
                value_list = self._validate_value_list(body)
            except (ValueError, TypeError) as e:
                return jsonify({"status": "error", "message": str(e)}), 400

            calculator = SecondCalculator(value_list)
            result = calculator.calculate()

            return jsonify({"status": "success",
                        "result": result})
        

        @self.app.route('/third', methods=["POST"])
        def third_calculator():
            body = request.get_json()
            try:
                value_list = self._validate_value_list(body)
            except (ValueError, TypeError) as e:
                return jsonify({"status": "error", "message": str(e)}), 400

            calculator = ThirdCalculator(value_list)
            result = calculator.compare()

            if result:
                return jsonify({"status": "success",
                        "message": "success proceed"})
            
            return jsonify({"status": "fail",
                        "message": "failed proceed"})

    def _validate_value(self, body: dict) -> float:
        if not body or "value" not in body:
            raise ValueError("Missing 'value' in request body.")
        try:
            value = float(body["value"])

        except (ValueError, TypeError):
            raise TypeError("'value' must be a number.")
        
        return value

    def _validate_value_list(self, body: dict) -> list[float]:
        if not body or "value_list" not in body:
            raise ValueError("Missing 'value_list' in request body.")

        value_list = body["value_list"]

        if not isinstance(value_list, list):
            raise TypeError("'value_list' must be a list")

        if not all(isinstance(x, (int, float)) for x in value_list):
            raise TypeError("All elements in 'value_list' must be numbers.")

        if len(value_list) == 0:
            raise ValueError("'value_list' cannot be empty.")
        
        return value_list
