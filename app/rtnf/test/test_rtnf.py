from datetime import datetime
import unittest
from ..src.rtnf import is_datetime_object, to_rtn_time, to_rtn_datetime


class TestDateTimeConversion(unittest.TestCase):

    def test_is_datetime_object(self):
        # Test with a valid datetime object
        datetime_obj = datetime.now()
        self.assertTrue(is_datetime_object(datetime_obj))

        # Test with an invalid object
        invalid_obj = "2023-05-21"
        self.assertFalse(is_datetime_object(invalid_obj))

    def test_to_rnt_time(self):
        # Test with a valid datetime object
        datetime_obj = datetime(2023, 9, 30, 19, 0)
        expected_result = "1900"
        self.assertEqual(to_rtn_time(datetime_obj), expected_result)

        # Test with an invalid object
        invalid_obj = "2023-05-21"
        with self.assertRaises(ValueError):
            to_rtn_time(invalid_obj)

    def test_to_rnt_datetime(self):
        # Test with a valid datetime object
        datetime_obj = datetime(2023, 5, 30, 19, 0)
        expected_result = "301900"
        self.assertEqual(to_rtn_datetime(datetime_obj), expected_result)

        # Test with an invalid object
        invalid_obj = "2023-05-21"
        with self.assertRaises(ValueError):
            to_rtn_datetime(invalid_obj)
