from flask import jsonify

# Error messages
INVALID_DIMENSIONS = "Input should be a list of four numeric values representing iris dimensions. Example: {'iris_dimensions': [5.0, 3.6, 1.4, 0.2]}"
ERROR_MESSAGE = "There was an unexpected error while processing your request."
PREDICTION_FAILED = "Failed to perform the prediction. Please check the provided input."


class CustomException(Exception):
    """
    Custom exception class for handling specific errors.
    """

    def __init__(self, message):
        """
        Constructor to initialize the CustomException class.

        Args:
            message (str): Error message for the exception.
        """
        super().__init__(message)
        self.message = message


def generate_error_response(error):
    """
    Generates an error response in JSON format.

    Args:
        error (CustomException): CustomException object with error message.

    Returns:
        response: Flask response object with error message and status code 400.
    """
    response = jsonify({"error": error.message})
    response.status_code = 400
    return response
