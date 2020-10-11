"""Author: Nikhil Kalyan
    Date: Sunday Sep Oct 10, 2020 9:00 PM
    The following file contains User Story 11 of sprint 1 which used to find if there is ant bigamy in GedCom file
    Written each test case at one time and ran code and again rerun for other test cases as follows

This code is pristine which is free some bad smells like previous one, this is do not have instances and variable
that are been not used or left alone in previous code
BadSmell 1: Removed method popped because there is no use of writing separate for popping names if they are
            bigamy or illegal we can directly do it if that meet some criteria
BadSmell 2: Printing output directly in console rather writing it in separate file
BadSmell 3: Reduced supplying unwanted parameters
BadSmell 4: Reduced Cyclomatic complexity by writing other method to get id's removed for loop and nested if statements"""

import unittest
from typing import Dict, List


def getID(family: Dict):
    """Returns Husband n wife ID's"""
    for f in family:
        if 'HUSB' in family[f]:
            hus_id = family[f]['HUSB']
            if 'WIFE' in family[f]:
                wife_id = family[f]['WIFE']
    return hus_id, wife_id


def checkBigamy(family: Dict, indi: Dict):
    """Method that checks bigamy in the given gedcom data if yes then it pops and update data with no bigamy"""
    hus_id, wife_id = getID(family)

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
    if husb_count > 1 or wife_count > 1:
        """if bigamy occurs, remove both instances of a spouse"""
        print("ERROR US11: Marriage should not occur during marriage to another spouse\n")
        family.pop(hus_id, wife_id)
        indi.pop(hus_id, wife_id)


class TestCases(unittest.TestCase):
    def test_checkBigamy(self):
        """Test cases for bigamy"""
        # No Bigamy
        fam: Dict = {'F23':
                         {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                          'CHIL': ['I19', 'I26', 'I30']},
                     'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}

        indi: Dict = {
            'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                    'DEAT': '31 DEC 2013'},
            'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F',
                    'family': 'F23'},
            'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
            'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
            'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
            'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
            'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F',
                    'family': 'F23'}}

        # bigamy (same husband)
        fam2: Dict = {'F23':
                          {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                           'CHIL': ['I19', 'I26', 'I30']},
                      'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'HUSB': 'I01'}}

        indi2: Dict = {
            'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                    'DEAT': '31 DEC 2013'},
            'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F',
                    'family': 'F23'},
            'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
            'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
            'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
            'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
            'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F',
                    'family': 'F23'}}

        # bigamy (same wife)
        fam3: Dict = {'F23':
                          {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                           'CHIL': ['I19', 'I26', 'I30']},
                      'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'WIFE': 'I07'}}

        indi3: Dict = {
            'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                    'DEAT': '31 DEC 2013'},
            'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F',
                    'family': 'F23'},
            'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
            'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
            'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
            'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
            'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F',
                    'family': 'F23'}}

        checkBigamy(fam, indi)
        self.assertTrue(('I01' in indi))
        self.assertTrue(('I01' == fam['F23']['HUSB']))
        checkBigamy(fam2, indi2)
        self.assertFalse(('I02' in indi2))
        self.assertTrue(('I02' not in fam2['F23']['HUSB']))
        checkBigamy(fam3, indi3)
        self.assertTrue(('I07' in indi3))
        self.assertTrue(('WIFE' in fam3['F23']))


if __name__ == "__main__":
    """Main"""
    unittest.main(exit=True, verbosity=2)
