from flask import jsonify

INVALID_DIMENSIONS = "Input should be a list of four numeric values representing iris dimensions. Example: {'iris_dimensions': [5.0, 3.6, 1.4, 0.2]}"
ERROR_MESSAGE = "There was an unexpected error while processing your request."
PREDICTION_FAILED = "Failed to perform the prediction. Please check the provided input."


class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def generate_error_response(error):
    response = jsonify({"error": error.message})
    response.status_code = 400
    return response
