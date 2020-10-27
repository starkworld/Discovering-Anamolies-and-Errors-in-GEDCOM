import unittest
from typing import List

from Source.gedcom_parsor import findParents, checkIfSiblings
from Source.famclass import gedFileParse

individual, families = gedFileParse("/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/CFMT.ged")


def firstCousinShouldNotMarry() -> List:
    """ check if parents of husband and spouse. If parents are siblings in each others families then first cousins.
    Return """

    listFam: List = families

    individualError: List = []

    for fam in listFam:
        if fam[1] != 'NA' and fam[2] != 'NA':
            husbParents: str = findParents(fam[1], listFam)
            wifeParents: str = findParents(fam[2], listFam)
            if husbParents and wifeParents:
                siblings: bool = checkIfSiblings(husbParents, wifeParents, listFam)
                if siblings:
                    individualError.append(fam)
    return individualError


class TestApp(unittest.TestCase):
    def test_firstCousinShouldNotMarry(self):
        """Test Cases for User Story 19"""
        errorList: List = firstCousinShouldNotMarry()
        for fam in errorList:
            print(
                "ERROR: FAMILY: US19: In Family id " + fam.id + " Husband " + fam.husb + "Married to first cousin, "
                                                                                         "Wife " + fam.wife)
        self.assertTrue(len(errorList) == 0, "US19: No first cousins are married!")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)