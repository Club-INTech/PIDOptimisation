import unittest
from logger import logger
from GA.individual_class import Individual


class LoggerTest(unittest.TestCase):

    def test_correct_log_individual(self):
        file = logger.define_file("test_logs", test=True)
        individual = Individual()
        s = [12.12, 12.13, 13.14]
        t = [0, 1, 2]
        individual.set_s_t(s, t)
        logger.save_individual(file, individual, 5)
        file.close()
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
