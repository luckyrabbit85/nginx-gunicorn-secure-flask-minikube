import logging


def setup_app_logger(name):
    """
    Set up a custom logger for the application.

    Args:
        name (str): Name of the logger.

    Returns:
        logging.Logger: Configured logger instance.

    This function configures a custom logger for the application with a
    specified name and a basic stream handler.

    The `name` parameter represents the name of the logger, facilitating log identification
    within the application. The function sets up a logger instance using the `logging` module
    and configures it to output log messages to the console via a stream handler.

    The logger instance's level is set to `DEBUG`, allowing it to capture all log messages. It
    then adds the stream handler configured with a specific log message format to the logger.

    Returns the configured logger instance for use within the application. The logger can be
    accessed throughout the application to record log messages and assist in debugging and monitoring.
    """
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger
