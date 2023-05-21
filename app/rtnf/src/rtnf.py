from datetime import datetime


def is_datetime_object(datetime_to_check: datetime):
    """
    Check if the given object is an instance of the datetime class.

    Args:
        datetime_to_check: The object to check.

    Returns:
        bool: True if the object is a datetime object, False otherwise.
    """

    return isinstance(datetime_to_check, datetime)

