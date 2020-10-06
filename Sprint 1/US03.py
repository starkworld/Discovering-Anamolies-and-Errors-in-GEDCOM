"""
Author: Nikhil Kalyan
Time: 04 Oct, 202o 6:48PM
Implementing user story 3 which is children birth that happened before spouse death
"""
import unittest
from datetime import datetime


def birthBeforeDeath(ind, file):
    result = True
    for i in ind:
        if "BIRT" in ind[i] and "DEAT" in ind[i]:
            birthday = datetime.strptime(ind[i]["BIRT"], '%d %b %Y')
            deathday = datetime.strptime(ind[i]["DEAT"], '%d %b %Y')
            if birthday > deathday:
                file.write("ERROR US03: Birth of " + i + " comes before their death\n")
                result = False
    return result


class TestMethods(unittest.TestCase):
    def test_birthBeforeDeath(self):
        file = open('Output.txt', 'a+')
        ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
                'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1999', 'sex': 'M', 'family': 'F23'},
                'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23'},
                'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12'},
                'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010', 'sex': 'M', 'family': 'F12'},
                'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997', 'sex': 'M', 'family': 'F23'},
                'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005', 'sex': 'F', 'family': 'F16'},
                'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003', 'sex': 'M', 'family': 'F16'}}

        ind4 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1999', 'sex': 'M', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23'},
                'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12'},
                'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010', 'sex': 'M', 'family': 'F12'},
                'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997', 'sex': 'M', 'family': 'F23'},
                'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005', 'sex': 'F', 'family': 'F16'},
                'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003', 'sex': 'M', 'family': 'F16'}}
        ind5 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 2015', 'sex': 'M', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1999', 'sex': 'M', 'family': 'F23',
                        'DEAT': '31 DEC 2013'},
                'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23'},
                'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12'},
                'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010', 'sex': 'M', 'family': 'F12'},
                'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997', 'sex': 'M', 'family': 'F23'},
                'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005', 'sex': 'F', 'family': 'F16'},
                'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003', 'sex': 'M', 'family': 'F16'}}

        self.assertTrue(birthBeforeDeath(ind3, file))
        self.assertTrue(birthBeforeDeath(ind4, file))
        self.assertFalse(birthBeforeDeath(ind5, file))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
