"""
Author: Nikhil Kalyan
Time: 04 Oct, 202o 7:15PM
Implementing user story 8 which identified children birth before marriage or parents who gaven birth before marriage
"""

import unittest
from datetime import datetime
from typing import TextIO, Tuple


def birthBeforeMarriage(childsname: str, childsid: str, childsbirthday: str, marrdate: str, divdate: str,
                        divBool: bool) -> \
        Tuple[bool, bool]:
    error_div: bool = False
    error_bir: bool = False
    if ((datetime.strptime(marrdate, '%d %b %Y')) < (datetime.strptime(childsbirthday, '%d %b %Y')) and (
            divBool == True)):
        date_birth: datetime = datetime.strptime(childsbirthday, '%d %b %Y')
        date_div: date_birth = datetime.strptime(divdate, '%d %b %Y')
        dif_time: float = ((date_birth - date_div).days / 365.25) * 12
        if dif_time > 9:
            f: TextIO = open("Output.txt", "a+")
            f.write(
                "Error US08: Birthdate of child " + childsname + " (" + childsid + ") is >9 months after their "
                                                                                   "parents' divorce.\n")
            f.close()
            error_div: bool = True
    elif (datetime.strptime(marrdate, '%d %b %Y')) > (datetime.strptime(childsbirthday, '%d %b %Y')):
        f: TextIO = open("Output.txt", "a+")
        f.write(
            "Error US08: Birthdate of child " + childsname + " (" + childsid + ") is before their parents' marriage.\n")
        f.close()
        error_bir: bool = True
    return error_bir, error_div


class MyTest(unittest.TestCase):
    def test_birthBeforeMarriage(self):
        childName: str = "idk"
        childID: str = "I30"
        childBirthday: str = "15 JUN 1980"
        marriageDate: str = "15 JUL 1980"
        divorceDate: str = "----"
        divBool: bool = False
        error_birth, error_div = birthBeforeMarriage(childName, childID, childBirthday, marriageDate, divorceDate,
                                                     divBool)
        self.assertEqual(error_birth, True)
        self.assertEqual(error_div, False)
        childBirthday: str = "15 JUN 1985"
        birthBeforeMarriage(childName, childID, childBirthday, marriageDate, divorceDate, divBool)
        self.assertEqual(error_birth, False)
        divorceDate: str = "14 JUN 1983"
        childBirthday: str = "15 JUN 1985"
        birthBeforeMarriage(childName, childID, childBirthday, marriageDate, divorceDate, divBool)
        self.assertEqual(error_div, True)
        birthBeforeMarriage(childName, childID, childBirthday, marriageDate, divorceDate, divBool)
        self.assertEqual(error_birth, False)


if __name__ == '__main__':
    unittest.main()
