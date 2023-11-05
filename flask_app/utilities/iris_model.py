import pickle
import numpy as np
from flask import jsonify, Request
from typing import List, Dict
from utilities.error_handler import CustomException
from utilities.error_handler import (
    INVALID_DIMENSIONS,
    ERROR_MESSAGE,
    PREDICTION_FAILED,
)

MODEL_PATH: str = "models/SVM_20231027134419.pkl"


class IrisModel:
    """Handles iris data validation and prediction using a pre-loaded model."""

    def __init__(self, model_path: str = MODEL_PATH) -> None:
        """
        Initialize the IrisModel.

        Args:
            model_path (str): The path to the pre-trained model file.
        """
        try:
            with open(model_path, "rb") as model_file:
                self.model = pickle.load(model_file)
        except Exception:
            raise CustomException(ERROR_MESSAGE)

    def validate_iris_dimensions(self, json_data: Dict[str, List[float]]) -> np.ndarray:
        """
        Validates iris data dimensions.

        Args:
            json_data (Dict[str, List[float]]): The JSON data containing 'iris_dimensions'.

        Returns:
            np.ndarray: Numpy array of the validated iris dimensions.
        Raises:
            CustomException: If dimensions are invalid.
        """
        iris_dimensions = json_data.get("iris_dimensions")
        if "iris_dimensions" not in json_data:
            raise CustomException(INVALID_DIMENSIONS)
        if not isinstance(iris_dimensions, list):
            raise CustomException(INVALID_DIMENSIONS)
        if len(iris_dimensions) != 4:
            raise CustomException(INVALID_DIMENSIONS)
        if not all(isinstance(x, (int, float)) for x in iris_dimensions):
            raise CustomException(INVALID_DIMENSIONS)

        return np.array(iris_dimensions).reshape(1, -1)

    def predict(self, request: Request) -> jsonify:
        """
        Predicts iris type based on provided data.

        Args:
            request (Request): The request containing JSON data.

        Returns:
            jsonify: JSON response with predicted iris type.
        Raises:
            CustomException: If prediction fails.
        """
        json_data = request.json
        iris_dimensions = self.validate_iris_dimensions(json_data)
        try:
            result = self.model.predict(iris_dimensions)
            return jsonify({"iris_type": result[0]})
        except Exception:
            raise CustomException(PREDICTION_FAILED)
