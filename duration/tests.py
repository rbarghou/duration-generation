import time
from unittest import TestCase

from . import duration


class DurationBasicUseCases(TestCase):

    def test_one_second_loop(self):
        """
        Tests that a duration of one second really does take that long.
        :return:
        """
        before = time.time()
        for k in duration(1.0):
            pass
        after = time.time()

        d = after - before

        self.assertGreaterEqual(d, 1, "The loop took less than one second.")

        self.assertGreaterEqual(k, 0, "The loop should have at least executed once.")
