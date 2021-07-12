#Day 20 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Testing code using unit testing--###

import unittest

from city_country import *

class testCC(unittest.TestCase):

    def testCC(self):
        formatted_CC = city_country('madrid', 'spain')
        self.assertEqual(formatted_CC, 'Madrid, Spain')
    
    #Testing in the population function
    def testCCPop(self):
            formatted_CC = city_country_pop('madrid', 'spain', 50000)
            self.assertEqual(formatted_CC, 'Madrid, Spain: 50000')

    #Testing that the population function also works without population parameter in place
    def testCCPop_noPop(self):
        formatted_CC = city_country_pop('madrid', 'spain')
        self.assertEqual(formatted_CC, 'Madrid, Spain')

if __name__ == '__main__':
    unittest.main()

#Use print for in code testing and return for unittesting
#Was not working before becuase I had my city_country code set to print out rather than return

    
    

if __name__ == '__main__':
    unittest.main()
