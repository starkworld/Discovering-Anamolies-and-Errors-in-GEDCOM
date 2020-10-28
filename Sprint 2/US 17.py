from datetime import datetime, date
import unittest
from typing import List


def age(dat):
    """ calculate age using the birth date """
    today = date.today()
    birthday = datetime.strptime(dat['date'], "%d %b %Y")
    age = today.year - birthday.year - \
          ((today.month, today.day) < (birthday.month, birthday.day))
    return age


def individual_ages(individuals: List):
    list_of_ages = []
    for individual in individuals:
        list_of_ages.append(age(individual))
    print("List of individual age -", list_of_ages)
    return list_of_ages


class TestCase(unittest.TestCase):
    def test_individual_ages(self):
        indi1 = {'date': "14 OCT 1990"}
        indi2= {'date': "24 OCT 1991"}
        indi3 = {'date': "4 OCT 1992"}
        indi4 = {'date': "5 OCT 1993"}
        indi5= {'date': "6 OCT 2000"}
        indi6= {'date': "7 OCT 1999"}
        individuals: List = [indi1, indi2, indi3, indi4, indi5, indi6]
        self.assertEqual(individual_ages(individuals), [30, 29, 28, 27, 20, 21])

        indi1 = {'date': "1 OCT 2000"}
        indi2 = {'date': "2 OCT 2001"}
        indi3 = {'date': "3 OCT 2002"}
        indi4 = {'date': "4 OCT 2003"}
        indi5 = {'date': "5 OCT 2004"}
        indi6 = {'date': "6 OCT 2005"}
        individuals: List = [indi1, indi2, indi3, indi4, indi5, indi6]
        self.assertEqual(individual_ages(individuals), [20, 19, 18, 17, 16, 15])

        indi1 = {'date': "14 OCT 2016"}
        indi2 = {'date': "24 OCT 2015"}
        indi3 = {'date': "4 OCT 2014"}
        indi4 = {'date': "5 OCT 2013"}
        indi5 = {'date': "6 OCT 2012"}
        indi6 = {'date': "7 OCT 2011"}
        individuals: List = [indi1, indi2, indi3, indi4, indi5, indi6]
        self.assertNotEqual(individual_ages(individuals), [4, 5, 6, 7, 8, 0])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
