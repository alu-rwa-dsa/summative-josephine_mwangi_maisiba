import unittest
from HighFidelity.main import *


class Testcreatingframe(unittest.TestCase):
     def create_frame(self):
        self.assertTrue(create_frame(40, 0, 20))

     def drawpathbacktostart(self):
         self.assertTrue(shortestpath_backtostart(400, 400))

     def draw_maze(self):
        self.assertTrue(create_maze(20, 20))


if __name__ == "__main__":
    unittest.main()
