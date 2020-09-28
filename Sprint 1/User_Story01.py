"""Author: Nikhil Kalyan
    Date: Sunday Sep 27, 2020 9:00 PM
    Description: Implementing User story 01 in sprint 1 by writing each test cases for each iteration"""

import unittest
import datetime
from typing import List

from famclass import gedFileParse

individual, family = gedFileParse("/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/CFMT.ged")


def us_01(indi: List[str], fam: List[str]) -> List:
    """Method that returns birth, death, marriage and divorce date before today"""
    lst: List = []
    for person in indi:
        if person[3] and person[4] != 0:
            lst.append(datetime.datetime.strptime(person[3], '%Y %b %d'))
            lst.append(datetime.datetime.strptime(person[4], '%Y %b %d'))
    for person in fam:
        if person[3] and person[4] != 0:
            lst.append(datetime.datetime.strptime(person[3], '%Y %b %d'))
            lst.append(datetime.datetime.strptime(person[4], '%Y %b %d'))
    return lst


class TestGedcomParsor(unittest.TestCase):
    """Class of that contains test suite"""

    def test_us_01(self):
        current_time = datetime.datetime.now()
        for result in us_01(individual, family):
            self.assertLess((result - current_time).days, 0)
            self.assertGreater((current_time - result).days, 0)
            self.assertTrue((current_time - result).days > 0)
            self.assertFalse((current_time - result).days < 0)
            self.assertNotEqual(result, current_time)


if __name__ == "__main__":
    unittest.main(exit=True, verbosity=2)
