"""Author: Nikhil Kalyan
    Date: Sunday Sep 27, 2020 9:00 PM
    The following file contains User Story 11 of sprint 1 which used to find if there is ant bigamy in GedCom file
    Written each test case at one time and ran code and again rerun for other test cases as follows
     BadeSmell 1: Nested Loops in checkBigamy
     BadSemll 2: Unwanted Parameters supply i.e file
     BadSmell 3: Writing output
     BadSmell 4: Methods that are not very much used or helpful i.e popped()"""

import unittest
from typing import List, Dict, TextIO


def checkBigamy(family: Dict, file: TextIO):
    """Method that checks bigamy in the given gedcom data if yes then it pops and update data with no bigamy"""
    for f in family:
        if 'HUSB' in family[f]:
            hus_id = family[f]['HUSB']
            if 'WIFE' in family[f]:
                wife_id = family[f]['WIFE']

        wife_count = 0
        husb_count = 0

        for f in family:
            if 'HUSB' in family[f]:
                hus_id2: List = family[f]['HUSB']
                if hus_id == hus_id2:
                    husb_count += 1
                if 'WIFE' in family[f]:
                    wife_id2: List = family[f]['WIFE']
                    if wife_id == wife_id2:
                        wife_count += 1
            else:
                continue

            if husb_count > 1:
                """if bigamy occurs, remove both instances of a spouse"""
                file.write("ERROR US11: Marriage should not occur during marriage to another spouse\n")
                fam.pop(hus_id, None)
                indi.pop(hus_id, None)
                break
            if wife_count > 1:
                file.write("ERROR US11: Marriage should not occur during marriage to another spouse\n")
                fam.pop(hus_id, None)
                indi.pop(hus_id, None)
                break


def popped(lst: str):
    """Method takes list as argument pops value from list if list value is bigamy"""
    fam.pop(lst, None)
    indi.pop(lst, None)


# No Bigamy
fam = {'F23':
           {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
       'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}

indi = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                'DEAT': '31 DEC 2013'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

# bigamy (same husband)
fam2 = {'F23':
            {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'HUSB': 'I01'}}

indi2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                 'DEAT': '31 DEC 2013'},
         'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
         'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

# bigamy (same wife)
fam3 = {'F23':
            {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'WIFE': 'I07'}}

indi3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                 'DEAT': '31 DEC 2013'},
         'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
         'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


class gedComTestCases(unittest.TestCase):
    """Unit test suite"""

    def test_checkBigamy(self):
        """Test cases for bigamy"""
        f = open('output1.txt', 'a+')
        checkBigamy(fam,f)
        self.assertTrue(('I01' in indi))
        self.assertTrue(('I01' == fam['F23']['HUSB']))
        checkBigamy(fam2,f)
        self.assertTrue(('I01' in indi2))
        self.assertTrue(('I01' in fam2['F23']['HUSB']))
        checkBigamy(fam3,f)
        self.assertTrue(('I07' in indi3))
        self.assertTrue(('WIFE' in fam3['F23']))


if __name__ == "__main__":
    """Main"""
    unittest.main(exit=True, verbosity=2)
