"""
    Author: Nikhil Kalyan
    Time and Date: 04 Oct, 2020 2:33PM
    Implementing User Story that says Marriage of persons have to occur after 14 years from birth date
"""
from datetime import datetime
import unittest
from typing import Union, List, TextIO, Dict


def getAge(born: str) -> Union[int, bool]:
    """returns age of individual"""
    born: datetime = datetime.strptime(born, '%d %b %Y')
    today: datetime = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def getAgeAt(born: str, given: str) -> Union[int, bool]:
    born: datetime = datetime.strptime(born, '%d %b %Y')
    given: datetime = datetime.strptime(given, '%d %b %Y')
    return given.year - born.year - ((given.month, given.day) < (born.month, born.day))


def marrAfter14(fam: Dict, ind: Dict, file: TextIO):
    result: bool = True

    for f in fam:
        if "HUSB" in fam[f]:
            husb: int = fam[f]["HUSB"]
            if husb in ind and "BIRT" in ind[husb]:
                age: int = 0
                if "MARR" in fam[f]:
                    age: int = getAgeAt(ind[husb]["BIRT"], fam[f]["MARR"])
                if age <= 14:
                    file.write("ERROR: US10 - The individual " + husb + " was married before 14, this is invalid\n")
                    result: bool = False
        if "WIFE" in fam[f]:  # check wife age
            wife: int = fam[f]["WIFE"]
            if wife in ind and "BIRT" in ind[wife]:
                age: int = 0
                if "MARR" in fam[f]:
                    age: int = getAge(ind[wife]["BIRT"])
                if age <= 14:
                    file.write("ERROR: US10 - The individual " + wife + " was married before 14, this is invalid\n")
                    result: bool = False
    return result


class TestMethods(unittest.TestCase):
    def test_marrAfter14(self):
        f: TextIO = open('Output.txt', 'a+')
        ind: Dict = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                             'DEAT': '31 DEC 2013'},
                     'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F',
                             'family': 'F23'},
                     'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
                     'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
                     'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12'},
                     'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F12'},
                     'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
                     'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981', 'sex': 'F',
                             'family': 'F16'},
                     'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981', 'sex': 'M',
                             'family': 'F16'}}
        fam: Dict = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                             'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
                     'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'HUSB': 'I45', 'WIFE': 'I44'},
                     'F12': {'fam': 'F12', 'MARR': '12 DEC 2008', 'DIV': '12 DEC 2001', 'HUSB': 'I32', 'WIFE': 'I30'}}
        fam2: Dict = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                              'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
                      'F16': {'fam': 'F16', 'MARR': '12 DEC 1990', 'HUSB': 'I45', 'WIFE': 'I44'},
                      'F12': {'fam': 'F12', 'MARR': '12 DEC 2008', 'DIV': '12 DEC 2019', 'HUSB': 'I32', 'WIFE': 'I30'}}

        self.assertTrue(marrAfter14(fam, ind, f))
        self.assertFalse(marrAfter14(fam2, ind, f))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
