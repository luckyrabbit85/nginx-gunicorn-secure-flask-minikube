import os
import logging
import requests
import json

from dotenv import load_dotenv

dotenv_path = ".env"
load_dotenv(dotenv_path)
slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")


class SlackHandler(logging.Handler):
    """Custom logging handler for sending log messages to Slack."""

    def __init__(self, webhook_url):
        """Initialize the SlackHandler with the specified Slack webhook URL."""
        logging.Handler.__init__(self)
        self.webhook_url = webhook_url

    def emit(self, record):
        """Emit a log record to Slack."""
        log_entry = self.format(record)
        payload = {"text": log_entry}
        headers = {"Content-type": "application/json"}
        requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)


def setup_logger(app, slack_webhook_url=None):
    """
    Set up the logger for the Flask application.

    Args:
        app (Flask): The Flask application instance.
        slack_webhook_url (str, optional): The Slack webhook URL for additional logging to Slack.

    Returns:
        logging.Logger: The configured logger.

    Note:
        This function configures the logger based on the Gunicorn logger and optionally adds a
        SlackHandler for additional logging to Slack.
    """
    # Set up the Gunicorn logger
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    # Add additional handler (SlackHandler) if Slack webhook URL is provided
    if slack_webhook_url:
        slack_handler = SlackHandler(slack_webhook_url)
        slack_handler.setLevel(logging.ERROR)  # Set the level as needed
        app.logger.addHandler(slack_handler)

    return app.logger  # Return the configured logger
