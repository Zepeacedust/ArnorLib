import unittest
from ArnorLib.Datatypes import Vector


class VectorTestCase(unittest.TestCase):

    def test_eq(self):
        """Test Vector.__eq__ operator"""

        self.assertEqual(Vector(3, 2), Vector(3, 2))

    def test_addition(self):
        """ test Vector.__add__ operator """
        self.assertEqual(Vector(3, 2) + Vector(7, 8), Vector(10, 10))

    def test_addition(self):
        """ test Vector.__sub__ operator """
        self.assertEqual(Vector(10, 10) - Vector(7, 8), Vector(3, 2))
    
    
    def test_vector_addition(self):
        """ test Vector.__mul__ operator with two vectors"""
        self.assertEqual(Vector(9, 15) * Vector(2, 3), Vector(18, 45))
    
    
    def test_int_addition(self):
        """ test Vector.__mul__ operator between vector and int"""
        self.assertEqual(Vector(9, 15) * 3, Vector(27, 45))
    
    
    def test_vector_division(self):
        """ test Vector.__truediv__ operator with two vectors"""
        self.assertEqual(Vector(9, 15) / Vector(3, 5), Vector(3.0, 3.0))
    
    
    def test_int_division(self):
        """ test Vector.__truediv__ operator between vector and int"""
        self.assertEqual(Vector(9, 15) / 3, Vector(3, 5))
    
    def test_magnitude(self):
        """ test Vector.magnitude """
        self.assertEqual(Vector(3,4).magnitude,5)
    
    def test_sqrMagnitude(self):
        """ test Vector.sqrMagnitude """
        self.assertEqual(Vector(3,4).sqrMagnitude, 25)
    
    def test_clamp(self):
        """ test Vector.clamp """
        self.assertEqual(Vector(1,2).clamp(), Vector(0.5, 1.0))
    
    def test_normalied(self):
        """ test Vector.normalized """
        testVector = Vector(5,4).normalized
        self.assertEqual(testVector.x ** 2 + testVector.y ** 2, 1)
        
    def test_clone(self):
        """ test Vector.clone"""
        testVector = Vector(5,4)
        copyVector = testVector.copy()
        self.assert_(testVector == copyVector and not testVector is copyVector)


if __name__ == '__main__':
    unittest.main()
