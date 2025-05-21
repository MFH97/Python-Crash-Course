# test_cities.py

import unittest
from city_functions import get_cities_name

class NamesTestCase(unittest.TestCase):
    def test_city_country(self):
        # Test for city and country without population
        formatted_name = get_cities_name('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')  # Correct expected output

    def test_population(self):
        # Test with population
        formatted_name = get_cities_name('santiago', 'chile', 5000000)
        self.assertEqual(formatted_name, 'Santiago, Chile – population 5000000')

if __name__ == '__main__':
    unittest.main()
