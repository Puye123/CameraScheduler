import unittest
import sys
import datetime

sys.path.append('../')
from src.camera_scheduler import*

class TestMain(unittest.TestCase):
    def test_get_unique_name(self):
        
        test_list = [
            ("20180627_215010", 2018, 6, 27, 21, 50, 10),
            ("20180701_215010", 2018, 7, 1,  21, 50, 10),
            ("20180627_015010", 2018, 6, 27,  1, 50, 10),
            ("20180627_210110", 2018, 6, 27, 21,  1, 10),
            ("20180627_215001", 2018, 6, 27, 21, 50,  1),
        ]

        for expected, year, month, day, hour, minute, second in test_list:
            with self.subTest(expected=expected, year=year, month=month, day=day, hour=hour, minute=minute, second=second):
                date = datetime.datetime(year, month, day, hour, minute, second)
                actual = get_unique_name(date)
                self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
