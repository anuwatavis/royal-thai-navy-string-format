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


def to_rtn_time(datetime_to_convert: datetime):
    """
    Convert the given datetime object to a string in the Royal Thai Navy time format.

    Args:
        datetime_to_convert: The datetime object to convert.

    Returns:
        str: The converted time string in the Royal Thai Navy date format.

    Raises:
        ValueError: If the input is not a valid datetime object.
    """

    if not is_datetime_object(datetime_to_convert):
        raise ValueError("Input is not a valid datetime object.")

    rnt_time_format = datetime_to_convert.strftime('%H%M')
    return rnt_time_format


def to_rtn_datetime(datetime_to_convert: datetime):
    """
    Convert the given datetime object to a string in the Royal Thai Navy time format.

    Args:
        datetime_to_convert: The datetime object to convert.

    Returns:
        str: The converted time string in the Royal Thai Navy date format.

    Raises:
        ValueError: If the input is not a valid datetime object.
    """

    if not is_datetime_object(datetime_to_convert):
        raise ValueError("Input is not a valid datetime object.")

    rnt_datetime_format = datetime_to_convert.strftime('%d%H%M')
    return rnt_datetime_format
