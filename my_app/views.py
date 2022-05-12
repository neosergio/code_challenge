from flask import Blueprint, request, jsonify

from .calculate import calculate_max_area

main = Blueprint("main", __name__)


@main.route("/")
def main_index():
    return "Hello World"


@main.route("/calculate")
def call_calculate_function():
    area = None
    if numbers := request.args.get("numbers"):
        numbers = [int(number) for number in numbers.split(",") if number.isdigit()]
        if len(numbers) >= 2:
            area = calculate_max_area(numbers)
        else:
            return jsonify({"error": "no numbers in list"})
    return jsonify({"max_area": area})
