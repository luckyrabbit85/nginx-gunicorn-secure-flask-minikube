from flask import Flask, jsonify, request
from utilities.iris_model import IrisModel
from utilities.app_logger import setup_gunicorn_logger_with_slack_handler
from utilities.error_handler import CustomException, generate_error_response
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)
logger = setup_gunicorn_logger_with_slack_handler(__name__)


@app.route("/", methods=["GET"])
def check_app():
    """Handles requests to check the status of the application."""
    logger.info("Status: 200")
    return jsonify({"status": "application is running"}), 200


@app.route("/predict", methods=["POST"])
def predict_iris_type():
    """
    Handles prediction requests for iris types.

    Returns:
        jsonify: JSON response with predicted iris type.
    Raises:
        CustomException: If prediction fails.
    """
    try:
        iris_model = IrisModel()
        return iris_model.predict(request)
    except CustomException as e:
        logger.info(request.json)
        logger.error(f"CustomError: {str(e)}")
        return generate_error_response(e)


# FOR DEVELOPMENT PURPOSE ONLY
# Running app in Flask's built-in development server

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
