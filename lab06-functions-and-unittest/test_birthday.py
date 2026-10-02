import unittest
from birthday import *



class TestBirthDay(unittest.TestCase):

    #dictionary of test values
    myTestValues = {birthday(3,8,1981):"3/8/1981",
                    birthday(11,13,2009):"11/13/2009",
                    birthday (4,20,1977):"4/20/1977",
                    birthday(12,5,2011):"12/5/2011"}
    totalPoints = 0
    maxPoints = 4

    def tearDown(self):
        print("Total score is %d out of %d." %(self.totalPoints, self.maxPoints))

    def test_birthday(self):
        print("\nStarting birthday() test:")
        try:
            for key in self.myTestValues:
                self.assertEqual(self.myTestValues[key], key, msg="birthday() failed for value "+ str(key))
                self.totalPoints += 1
        except ValueError as errorInfo:
            print ("Could not convert to numeric data:" + str(errorInfo))





if __name__ == '__main__':
    unittest.main()