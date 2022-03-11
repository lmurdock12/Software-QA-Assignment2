import unittest
from unittest.mock import patch
from BMI import calculateBMI,categorizeBMI,get_user_input

class TestCalculateBMI(unittest.TestCase):

    def test_under(self):
        """ Height: 5'9
            Weight: 115
        """
        self.assertEqual(calculateBMI(5,9,115),17.4,"Should be 17.4")

    def test_normal(self):
        """ Height: 5'3
            Weight: 125 
        """
        self.assertEqual(calculateBMI(5,3,125),22.7,"Should be 22.7")


    def test_overweight(self):
        """ Height: 6'1
            Weight: 210 
        """
        self.assertEqual(calculateBMI(6,1,210),28.4,"Should be 28.4")

    def test_obese(self):
        """ Height: 5'10
            Weight: 250 
        """
        self.assertEqual(calculateBMI(5,10,250),36.7,"Should be 36.7")


class TestCategorizeBMI(unittest.TestCase):

    #Test functions for the underweight if statement
    def test_underweight_under(self):
        self.assertEqual(categorizeBMI(17.5),"underweight","Should be underweight")
    
    def test_underweight_min(self):
        self.assertEqual(categorizeBMI(18.4),"underweight","Should be underweight")

    def test_underweight_over(self):
        self.assertEqual(categorizeBMI(19.4),"normal weight","Should be normal weight")

    #Test functions for the normal weight if statement
    def test_normal_under(self):
        self.assertEqual(categorizeBMI(17.5),"underweight","Should be underweight")

    def test_normal_min(self):
        self.assertEqual(categorizeBMI(18.5),"normal weight","Should be normal weight")

    def test_normal_interior(self):
        self.assertEqual(categorizeBMI(21.75),"normal weight","Should be normal weight")

    def test_normal_max(self):
        self.assertEqual(categorizeBMI(24.9),"normal weight","Should be normal weight")

    def test_normal_over(self):
        self.assertEqual(categorizeBMI(26),"overweight","Should be overweight")

    #Test functions for the overweight if statement
    def test_overweight_under(self):
        self.assertEqual(categorizeBMI(24),"normal weight","Should be normal weight")

    def test_overweight_min(self):
        self.assertEqual(categorizeBMI(25),"overweight","Should be overweight")

    def test_overweight_interior(self):
        self.assertEqual(categorizeBMI(27.5),"overweight","Should be overweight")

    def test_overweight_max(self):
        self.assertEqual(categorizeBMI(29.9),"overweight","Should be overweight")

    def test_overweight_over(self):
        self.assertEqual(categorizeBMI(31),"obese","Should be obese")

    
    #Test functions for the obese if statement
    def test_obsese_under(self):
        self.assertEqual(categorizeBMI(29),"overweight","Should be overweight")

    def test_obese_min(self):
        self.assertEqual(categorizeBMI(30),"obese","Should be obese")

    def test_obese_over(self):
        self.assertEqual(categorizeBMI(31),"obese","Should be obese")

class TestUserInput(unittest.TestCase):

    @patch('__builtin__.input')
    def mock_get_user_input(self,mock_input):
        """ Test out the get_user_input function with mocked user input
        
            Height: 5'3"
            Weight: 125
        """
        mock_input.side_effect = ["5","3","125"]
        res = get_user_input()
        self.assertEqual(res[0],5)
        self.assertEqual(res[1],3)
        self.assertEqual(res[2],125)


if __name__ == '__main__':
    unittest.main()