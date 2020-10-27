import unittest
from typing import List

from gedcom_parsor import findParents, checkIfSiblings
from famclass import gedFileParse

individual, families = gedFileParse("/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/CFMT.ged")


def auntsAndUncle() -> List:
    listFam: List = families

    individualError: List = []
    for fam in listFam:
        if fam.husb != 'NA' and fam.wife != 'NA':
            husbParents: str = findParents(fam.husb, listFam)
            wifeParents: str = findParents(fam.wife, listFam)
            if husbParents and wifeParents:
                hSiblings: bool = checkIfSiblings(husbParents, fam, listFam)
                wSiblings: bool = checkIfSiblings(wifeParents, fam, listFam)
                if hSiblings:
                    individualError.append(fam)
                elif wSiblings:
                    individualError.append(fam)
    return individualError


class TestApp(unittest.TestCase):
    def test_auntsAndUncle(self):
        errorList: List = auntsAndUncle()
        for fam in errorList:
            print("ERROR: FAMILY: US20: " + fam.id + " Marriage is between Aunt/Uncle and Niece/Nephew!")
        self.assertTrue(len(errorList) == 0,
                        "US20: Marriages are correct and no one is married to an Aunt or Uncle!")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
