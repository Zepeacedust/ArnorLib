import unittest
from ArnorLib.Datatypes import Vector


class VectorTestCase(unittest.TestCase):

    def test_eq(self):
        """Test equality operator"""

        self.assertEqual(Vector(3,2), Vector(3,2))


if __name__ == '__main__':
    unittest.main()