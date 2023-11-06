import json
import logging
from logging.config import dictConfig
import requests
from dotenv import load_dotenv
import os

dotenv_path = "flask_app/.env"
load_dotenv(dotenv_path)

slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")


# for sending error logs to slack
class HTTPSlackHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        json_text = json.dumps({"text": log_entry})
        url = slack_webhook_url
        return requests.post(
            url, json_text, headers={"Content-type": "application/json"}
        ).content


def setup_app_logger(name, debug=True):
    logging.HTTPSlackHandler = HTTPSlackHandler
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": True,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                },
                "access": {
                    "format": "%(message)s",
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "stream": "ext://sys.stdout",
                },
                "slack": {
                    "class": "logging.HTTPSlackHandler",
                    "formatter": "default",
                    "level": "ERROR",
                },
            },
            "loggers": {
                "gunicorn.error": {
                    "handlers": ["console"],
                    "level": "INFO",
                    "propagate": False,
                },
                "gunicorn.access": {
                    "handlers": ["console"],
                    "level": "INFO",
                    "propagate": False,
                },
            },
            "root": {
                "level": "DEBUG" if debug else "INFO",
                "handlers": ["console"],
            },
        }
    )
    return logging.getLogger(name)
