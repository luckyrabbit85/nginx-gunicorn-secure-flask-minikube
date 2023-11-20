import time
import json
import socket
import logging
from flask import Flask, jsonify, request

from utilities.custom_logger_setup import setup_logger, slack_webhook_url
from utilities.custom_error_handler import CustomException, generate_error_response
from utilities.custom_prediction_model import IrisModel

import warnings

warnings.filterwarnings("ignore")

# Initialize the Flask app
app = Flask(__name__)

# Configure the logger using the setup_logger function
if __name__ != "__main__":
    # Configuration for logger when imported as a module
    logger = setup_logger(app, slack_webhook_url)
else:
    # Use the default Flask logger when run directly
    logger = app.logger
    app.logger.setLevel(logging.DEBUG)


@app.route("/", methods=["GET"])
def check_app():
    """Handles requests to check the status of the application."""
    logger.info("Status: 200")
    text = f"ML application is running in container ID: {socket.gethostname()}"
    return jsonify({"status": text}), 200


@app.route("/predict", methods=["POST"])
def predict_iris_type():
    """
    Handles prediction requests for iris types.

    Returns:
        jsonify: JSON response with predicted iris type.
    Raises:
        CustomException: If prediction fails.
    """
    start_time = time.time()
    try:
        iris_model = IrisModel()
    except CustomException as e:
        logger.error(f"Input JSON: {request.json}")
        logger.error(f"Failed loading model: {str(e)}")
        return generate_error_response(e)

    try:
        prediction_result = iris_model.predict(request)
        end_time = time.time()
        logger.info(f"Prediction took {end_time - start_time:.4f} seconds")
        return prediction_result
    except CustomException as e:
        logger.error(f"Input JSON: {request.json}")
        logger.error(str(e))
        return generate_error_response(e)


# FOR DEVELOPMENT PURPOSE ONLY
# Running app in Flask's built-in development server
if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
