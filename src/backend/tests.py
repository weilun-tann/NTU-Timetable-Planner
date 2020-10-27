import unittest

from src.backend.planner import Planner


class BackendTests(unittest.TestCase):
    def test_clashes(self):
        """
        ASSUMPTIONS
        1. BOUNDARY VALUES WILL REFER TO TIMESLOTS AT HALF-HOURLY INTERVALS (CONSIDER THE UNITS OF OUR USE CASE)
        2. LESSONS ARE 1-HOUR LONG TO AVOID HAVING TO CHANGE BOTH START AND END TIMES OF INTERVALS

        EC1 (VALID) : L <= FIXED
        EC2 (VALID) : L >= FIXED
        EC1 (INVALID) : L CROSSES FIXED IN FRONT
        EC2 (INVALID) : L CROSSES FIXED AT THE BACK
        """
        # EC1 (VALID)
        self.assertEqual(False, Planner.clashes([("MON", "09:30:00", "10:30:00"), ("MON", "10:30:00", "11:30:00")]))

        # EC2 (VALID)
        self.assertEqual(False, Planner.clashes([("MON", "11:30:00", "12:30:00"), ("MON", "10:30:00", "11:30:00")]))

        # EC3 (INVALID)
        self.assertEqual(True, Planner.clashes([("MON", "10:00:00", "11:00:00"), ("MON", "10:30:00", "11:30:00")]))

        # EC4 (INVALID)
        self.assertEqual(True, Planner.clashes([("MON", "11:00:00", "12:00:00"), ("MON", "10:30:00", "11:30:00")]))


if __name__ == "__main__":
    unittest.main()
