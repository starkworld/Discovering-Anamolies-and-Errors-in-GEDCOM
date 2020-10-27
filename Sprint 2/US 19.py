import unittest
from typing import List

from gedcom_parsor import findParents, checkIfSiblings
from famclass import gedFileParse

individual, families = gedFileParse("/Users/nikhilkalyan/Discovering-Anamolies-and-Errors-in-GEDCOM/CFMT.ged")


def firstCousinShouldNotMarry() -> List:
    """ check if parents of husband and spouse. If parents are siblings in each others families then first cousins.
    Return """

    listFam: List = families

    individualError: List = []

    for fam in listFam:
        if fam.husb != 'NA' and fam.wife != 'NA':
            husbParents: str = findParents(fam.husb, listFam)
            wifeParents: str = findParents(fam.wife, listFam)
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
