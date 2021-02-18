import unittest
from GA.sample_lib_utils import *
from GA.ga_pid_const import EPS

t1 = [0.05 * i for i in range(10)]
t2 = [0.05 * i for i in range(20)]

s1 = [i for i in range(20)]
s2 = [i for i in range(40)]
s3 = [0.01, 0.03, 0.1, 0.18, 0.26, 0.4, 0.7, 0.89, 0.97, 1.13, 1.17, 1.21, 1.12, 1.05, 0.90000001, 0.9, 0.9, 0.9, 0.9, 0.9]
s4 = [i for i in range(10)]


class SampleLibUtilsTest(unittest.TestCase):

    def test_is_ok_sample(self):
        self.assertFalse(is_sample_ok(s2, t2))
        self.assertFalse(is_sample_ok(s4, t1))
        self.assertTrue(is_sample_ok(s3, t2))

    def test_is_stable(self):
        self.assertFalse(is_stable(s2, EPS))
        self.assertTrue(is_stable(s3, EPS))

    def test_stat_error(self):
        self.assertTrue(abs(stat_error(s3, 1) - 0.1) <= EPS)

    def test_overflow(self):
        self.assertTrue(abs(overflow(s3) - 0.31) <= EPS)

    def test_T5(self):
        self.assertTrue(abs(response_time(s3, t2) - 0.7) <= EPS)


if __name__ == '__main__':
    unittest.main()
