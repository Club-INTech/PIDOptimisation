import unittest
from simulator.model import model_output
from simulator.model import S_vector, p, inverse_solution_matrix
import matplotlib.pyplot as pyplot


class SimulatorShowTest(unittest.TestCase):

    def test_show_model_output(self):
        s, t = model_output(1, 1.2, 0.002, 0.003)
        # vec = S_vector(1, p, 0.1, 0.1, 0.1)
        pyplot.plot(t, s)
        # pyplot.plot(p, vec)
        # print(inverse_solution_matrix(p, t)[0])
        pyplot.title("Model show test")
        pyplot.show()
        self.assertTrue(True)


if __name__ == '__main__':
        unittest.main()
