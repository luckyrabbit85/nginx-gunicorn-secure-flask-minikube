import json
import logging
from logging.config import dictConfig
import requests


# for sending error logs to slack
class HTTPSlackHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        json_text = json.dumps({"text": log_entry})
        url = "https://hooks.slack.com/services/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"
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
