import unittest
from simulator.model import model_output
import matplotlib.pyplot as pyplot


class SimulatorShowTest(unittest.TestCase):

    def test_show_model_output(self):
        s, t = model_output(1, 0.1, 0.1, 0.01)
        pyplot.plot(t, s)
        pyplot.title("Model show test")
        pyplot.show()
        self.assertTrue(True)


if __name__ == '__main__':
        unittest.main()
