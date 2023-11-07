import os
import json
import logging
from logging.config import dictConfig
import requests

from dotenv import load_dotenv

dotenv_path = ".env"
load_dotenv(dotenv_path)
webhook_url = os.getenv("SLACK_WEBHOOK_URL")


class SlackHandler(logging.Handler):
    """
    A handler class which sends log messages to a Slack channel using a webhook.
    """

    def __init__(self, webhook_url):
        """
        Initialize the handler.

        :param webhook_url: The webhook URL provided by Slack to send messages to a channel.
        """
        logging.Handler.__init__(self)
        self.webhook_url = webhook_url

    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the Slack via webhook.
        """
        log_entry = self.format(record)
        payload = {"text": log_entry}
        headers = {"Content-type": "application/json"}
        requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)


def setup_gunicorn_logger_with_slack_handler(name, debug=True):
    """
    Configure and return a logger with SlackHandler attached.

    Args:
    - name: Name for the logger.
    - log_config: Configuration for logging settings.
    - webhook_url: URL for the Slack webhook.

    Returns:
    - logger: Configured logger with SlackHandler attached.
    """
    # Configuration settings
    log_config = {
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
                "level": "DEBUG" if debug else "INFO",
                "formatter": "default",
            }
        },
        "loggers": {
            "root": {
                "level": "DEBUG" if debug else "INFO",
                "handlers": ["console"],
            },
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
    }

    # Apply configuration settings
    dictConfig(log_config)
    # Get a logger with a specific name
    logger = logging.getLogger(name)
    # Create a SlackHandler and add it to the logger
    slack_handler = SlackHandler(webhook_url)
    logger.addHandler(slack_handler)
    # Return the configured logger with the SlackHandler
    return logger
